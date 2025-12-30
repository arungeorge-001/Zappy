import pdfplumber
import pandas as pd
import re
from io import BytesIO


def extract_candidate_name(pdf):
    """
    Extract candidate name from the PDF.
    Looks for the Name field in the Candidate's Details section.
    """
    name = None

    # Read first page to get candidate name
    first_page = pdf.pages[0]
    text = first_page.extract_text()

    # Look for name in the Candidate's Details section
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if "Candidate's Details" in line:
            # Look for Name field in next few lines
            for j in range(i + 1, min(i + 10, len(lines))):
                if lines[j].strip().startswith('Name'):
                    # Extract name from the line
                    name_line = lines[j]
                    # Pattern: "Name" followed by the actual name
                    name_match = re.search(r'Name\s+(.+?)(?:\s*$)', name_line)
                    if name_match:
                        name = name_match.group(1).strip()
                        break
            break

    return name if name else "Unknown"


def extract_interview_level(text):
    """
    Extract interview level (L2, L3, or L4) from page text.
    """
    match = re.search(r'(L[234])\s+Interview\s+on', text)
    if match:
        return match.group(1)
    return None


def extract_table_data(page, interview_level):
    """
    Extract assessment data from tables on a page.
    Returns list of dictionaries with Assessment Area and Score.
    """
    data = []

    # Extract tables from the page
    tables = page.extract_tables()

    if not tables:
        return data

    # Find the assessment table (contains Sr. No, Assessment Area, Score columns)
    for table in tables:
        if not table or len(table) < 2:
            continue

        # Find the header row (may not be the first row)
        header_row = None
        header_row_idx = None
        sr_no_idx = None
        assessment_idx = None
        score_idx = None

        for idx, row in enumerate(table):
            if not row:
                continue

            # Check if this row contains the headers
            row_text = ' '.join([str(cell) if cell else '' for cell in row]).lower()

            if 'sr' in row_text and 'assessment' in row_text and 'score' in row_text:
                header_row = row
                header_row_idx = idx

                # Find column indices
                for col_idx, cell in enumerate(header_row):
                    if cell:
                        cell_lower = str(cell).lower()
                        if 'sr' in cell_lower and 'no' in cell_lower:
                            sr_no_idx = col_idx
                        elif 'assessment' in cell_lower:
                            assessment_idx = col_idx
                        elif 'score' in cell_lower:
                            score_idx = col_idx
                break

        # If we found the header row, process the data rows
        if header_row_idx is not None and all(x is not None for x in [sr_no_idx, assessment_idx, score_idx]):
            # Extract data rows (after the header)
            for row in table[header_row_idx + 1:]:
                if not row:
                    continue

                # Get Sr. No to check if it's a valid data row
                sr_no = str(row[sr_no_idx]).strip() if len(row) > sr_no_idx and row[sr_no_idx] else ''

                # Only process rows that have a numeric Sr. No
                if sr_no and sr_no.isdigit():
                    assessment_area = str(row[assessment_idx]).strip() if len(row) > assessment_idx and row[assessment_idx] else ''
                    score = str(row[score_idx]).strip() if len(row) > score_idx and row[score_idx] else ''

                    # Skip rows with empty assessment area or if assessment contains unwanted text
                    if assessment_area and assessment_area.lower() not in ['status', 'percentage', 'all interviewers']:
                        # Clean up score - keep numeric values or empty string
                        score_clean = score if score and (score.isdigit() or re.match(r'^\d+\.?\d*$', score)) else ''

                        data.append({
                            'Interview Level': interview_level,
                            'Assessment Area': assessment_area,
                            'Score': score_clean
                        })

    return data


def extract_assessment_data(pdf_file):
    """
    Main function to extract all assessment data from PDF.

    Args:
        pdf_file: Uploaded PDF file (BytesIO or file path)

    Returns:
        pandas DataFrame with columns: Name, Interview Level, Assessment Area, Score
    """
    all_data = []
    candidate_name = None

    try:
        # Open PDF
        if isinstance(pdf_file, str):
            pdf = pdfplumber.open(pdf_file)
        else:
            # For uploaded file from Streamlit
            pdf = pdfplumber.open(BytesIO(pdf_file.read()))

        # Extract candidate name from first page
        candidate_name = extract_candidate_name(pdf)

        # Process each page
        for page in pdf.pages:
            text = page.extract_text()

            # Extract interview level for this page
            interview_level = extract_interview_level(text)

            if interview_level:
                # Extract table data for this interview level
                page_data = extract_table_data(page, interview_level)
                all_data.extend(page_data)

        pdf.close()

        # Create DataFrame
        if all_data:
            df = pd.DataFrame(all_data)
            # Add candidate name to all rows
            df.insert(0, 'Name', candidate_name)

            # Reorder columns to match required format
            df = df[['Name', 'Interview Level', 'Assessment Area', 'Score']]

            return df
        else:
            return pd.DataFrame(columns=['Name', 'Interview Level', 'Assessment Area', 'Score'])

    except Exception as e:
        print(f"Error extracting data: {str(e)}")
        raise e


if __name__ == "__main__":
    # Test with sample file
    pdf_path = "Mukesh Kumar S_AssessmentSheet.pdf"
    df = extract_assessment_data(pdf_path)
    print(df)

    # Save to Excel
    df.to_excel("output.xlsx", index=False)
    print(f"\nData extracted successfully! Total records: {len(df)}")
