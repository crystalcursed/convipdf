import streamlit as st
import pymupdf4llm

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    df = extract_data(uploaded_file)

md_text = pymupdf4llm.to_markdown("uploaded_file.pdf")

# Write the text to some file in UTF8-encoding
import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())    