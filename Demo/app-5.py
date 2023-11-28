from dotenv import load_dotenv
import os
import streamlit as st
import openai
from PyPDF2 import PdfReader #  import pdf reader
from langchain.text_splitter import CharacterTextSplitter # import text splitter

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
   
            # # display the text on the streamlit app
            # st.write(text)

        # Use function from langchain to split the text into chunks
        text_splitter = CharacterTextSplitter(
            separator = "\n", # split by new line
            chunk_size = 1000, # split into chunks of 1000 characters
            chunk_overlap = 200, # overlap chunks by 200 characters
            length_function =  len # use the len function to get the length of the chunk
        )
        chunks = text_splitter.split_text(text)
        st.write(chunks) # display the text on the streamlit app  

if __name__ == '__main__':
    main()