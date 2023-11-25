from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader #  import pdf reader

# Take the pdf file and extract the text from it

def main():
    load_dotenv()
    # print(os.getenv("OPENAI_API_TYPE"))
    # print(os.getenv("OPENAI_API_VERSION"))
    # print(os.getenv("OPENAI_API_BASE"))
    # print(os.getenv("OPENAI_API_KEY"))

    st.set_page_config(
        page_title="Langchain Demo",
        page_icon="🔗",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.header("Talk to your PDF 💬")

    # Upload PDF file
    pdf = st.file_uploader("Upload PDF 📑")

    # check if user has uploaded a file
    # extract the text from the pdf file
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = "" # empty string to store the text
        for page in pdf_reader.pages: # for each page in the pdf
            text += page.extract_text() # concatenating all the text from the pages
  
            # display the text on the streamlit app
            st.write(text)


if __name__ == '__main__':
    main()