import streamlit as st
import pandas as pd
from pdf_extractor import extract_assessment_data
import io

# Set page configuration
st.set_page_config(
    page_title="Assessment Sheet Processor",
    page_icon="📄",
    layout="centered"
)

# Title and description
st.title("📄 Zappyhire Assessment Sheet Data Extractor")
st.markdown("Upload an assessment PDF file to extract candidate information and interview scores.")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=['pdf'],
    help="Upload the candidate assessment sheet in PDF format"
)

# Process button
if uploaded_file is not None:
    # Display file details
    st.success(f"File uploaded: {uploaded_file.name}")

    # Process file button
    if st.button("Process File", type="primary"):
        with st.spinner("Processing PDF file..."):
            try:
                # Extract data from PDF
                df = extract_assessment_data(uploaded_file)

                if df is not None and not df.empty:
                    st.success("Data extracted successfully!")

                    # Display the extracted data
                    st.subheader("Extracted Data Preview")
                    st.dataframe(df, use_container_width=True)

                    # Prepare Excel file for download
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, sheet_name='Assessment Data')

                    excel_data = output.getvalue()

                    # Download button
                    st.download_button(
                        label="📥 Download Excel File",
                        data=excel_data,
                        file_name=f"{uploaded_file.name.replace('.pdf', '')}_extracted.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

                    # Display statistics
                    st.subheader("Summary Statistics")
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric("Candidate Name", df['Name'].iloc[0] if not df.empty else "N/A")
                    with col2:
                        st.metric("Total Records", len(df))
                    with col3:
                        st.metric("Interview Levels", df['Interview Level'].nunique())

                else:
                    st.error("No data could be extracted from the PDF. Please check the file format.")

            except Exception as e:
                st.error(f"An error occurred while processing the file: {str(e)}")
                st.exception(e)

else:
    # Instructions when no file is uploaded
    st.info("👆 Please upload a PDF file to get started.")

    with st.expander("ℹ️ How to use this application"):
        st.markdown("""
        1. Click on the **Browse files** button above
        2. Select your assessment sheet PDF file
        3. Click the **Process File** button
        4. Review the extracted data in the preview table
        5. Click **Download Excel File** to save the results

        **Expected Output Format:**
        - Name: Candidate's name from the Candidate's Details section
        - Interview Level: L2, L3, or L4
        - Assessment Area: The skill/area being assessed
        - Score: The numeric score for each assessment area
        """)

# Footer
st.markdown("---")
st.markdown("*Assessment Sheet Data Extractor v1.0*")
