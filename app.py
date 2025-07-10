import streamlit as st
import pandas as pd
from utils.parsers import parse_file, detect_agency_from_text

st.set_page_config(page_title="Sales Report Parser", layout="wide")
st.title("📸 Sales Report Parser")

uploaded_file = st.file_uploader("Upload report (CSV or MHTML)", type=["csv", "mhtml"])
agency = st.selectbox("Select agency (or leave blank for auto-detect)", ["Auto", "NurPhoto", "EditorialFootage"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    filename = uploaded_file.name

    with st.spinner("Parsing report..."):
        if agency == "Auto":
            agency = detect_agency_from_text(file_bytes)

        df, parsed_agency = parse_file(file_bytes, agency, filename=filename)

        if df is not None and not df.empty:
            st.success(f"Parsed {parsed_agency} report with {len(df)} rows.")
            st.dataframe(df, use_container_width=True)
            csv = df.to_csv(index=False)
            st.download_button("Download CSV", csv, file_name=f"{parsed_agency}_report_parsed.csv", mime="text/csv")
        else:
            st.error("No usable data found. Please verify the file format.")
