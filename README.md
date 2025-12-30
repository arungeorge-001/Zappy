# Assessment Sheet Data Extractor

A Streamlit-based web application that extracts candidate assessment data from PDF files and exports it to Excel format.

## Features

- Upload PDF assessment sheets through a user-friendly web interface
- Automatically extract candidate name from Candidate's Details section
- Extract assessment data from multiple interview levels (L2, L3, L4)
- Filter only rows with numeric Sr. No values
- Generate Excel output with columns: Name, Interview Level, Assessment Area, Score
- Download extracted data as Excel file
- Display data preview and summary statistics

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. The application will open in your default web browser (usually at http://localhost:8501)

3. Upload your PDF assessment sheet using the file browser

4. Click the "Process File" button

5. Review the extracted data in the preview table

6. Download the Excel file using the "Download Excel File" button

## Output Format

The generated Excel file contains the following columns:

- **Name**: Candidate's name extracted from the Candidate's Details section
- **Interview Level**: The interview level (L2, L3, or L4)
- **Assessment Area**: The skill or area being assessed
- **Score**: The numeric score for each assessment area

## Example Output

| Name | Interview Level | Assessment Area | Score |
|------|----------------|-----------------|-------|
| Mukesh | L2 | Java | 8 |
| Mukesh | L3 | Automation Testing | 5 |
| Mukesh | L3 | Java | 4 |
| Mukesh | L3 | Cucumber | 0 |

## File Structure

```
.
├── app.py                  # Main Streamlit application
├── pdf_extractor.py        # PDF extraction logic
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Requirements

- Python 3.8 or higher
- streamlit 1.31.0
- pandas 2.1.4
- pdfplumber 0.10.3
- openpyxl 3.1.2

## How It Works

1. **PDF Parsing**: Uses pdfplumber to extract text and tables from the PDF
2. **Name Extraction**: Searches for the "Name" field in the Candidate's Details section
3. **Interview Level Detection**: Identifies L2, L3, and L4 sections in the document
4. **Table Extraction**: Extracts assessment tables and filters rows with numeric Sr. No
5. **Data Processing**: Combines all data into a structured format
6. **Excel Generation**: Creates an Excel file with the extracted data

## Notes

- Only rows with numeric values in the Sr. No column are extracted
- Empty scores are preserved in the output
- The application handles multiple interview levels in the same PDF
- All interview level data is combined into a single Excel file

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are installed correctly
2. Check that the PDF file follows the expected format
3. Verify that the PDF contains the required sections (Candidate's Details, L2/L3/L4 Interview tables)
4. Make sure the PDF is not password-protected or corrupted

## License

This project is open source and available for use and modification.
