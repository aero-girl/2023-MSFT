from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader #  import pdf reader
from langchain.text_splitter import CharacterTextSplitter # import text splitter

# Use function from langchain to split the text into chunks


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