from dotenv import load_dotenv
import os
import streamlit as st
import openai
from PyPDF2 import PdfReader #  import pdf reader

# Take the pdf file and extract the text from it

def main():
    load_dotenv()
    # Get API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY") 
    openai.api_base = os.getenv("OPENAI_API_BASE") 
    openai.api_type = os.getenv("OPENAI_API_TYPE")
    openai.api_version = os.getenv("OPENAI_API_VERSION")

    st.set_page_config(
        page_title="Chat 💬 with your PDF 📄",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.header("Talk to your PDF 💬")
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