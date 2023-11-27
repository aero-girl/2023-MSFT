from dotenv import load_dotenv
import os
import openai


import streamlit as st
from PyPDF2 import PdfReader #  import pdf reader
from langchain.text_splitter import CharacterTextSplitter # import text splitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from langchain.document_loaders import PyPDFLoader

# Use function from langchain to split the text into chunks


def main():
    load_dotenv()
    # print(os.getenv("OPENAI_API_TYPE"))
    # print(os.getenv("OPENAI_API_VERSION"))
    # print(os.getenv("OPENAI_API_BASE"))
    # print(os.getenv("OPENAI_API_KEY"))

   # Configure Azure OpenAI Service API
    # os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
    # os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    # os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
    # os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY") # set OpenAI API key
    print(f"OPENAI_API_KEY:{openai.api_key}") # print OpenAI API key
    openai.api_base = os.getenv("OPENAI_API_BASE") # set OpenAI Base URL
    print(f"OPENAI_API_BASE:{openai.api_base}") # print OpenAI Base URL

    openai.api_type = os.getenv("OPENAI_API_TYPE")
    openai.api_version = os.getenv("OPENAI_API_VERSION")

    st.set_page_config(
        page_title="Chat 💬 with your PDF 📄",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.header("Talk to your PDF 💬")

    # Upload PDF file
    pdf = st.file_uploader("Upload PDF 📑")

    # loader = PyPDFLoader(pdf)  
    # pages = loader.load_and_split()
    # st.write(pages)


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
        text_chunks = text_splitter.split_text(text)
        # st.write(chunks) # display the text on the streamlit app  

    #     # Define models
        model = "text-embedding-ada-002"
        completion_model = "gpt-35-turbo"

        # Create embeddings
        embeddings = OpenAIEmbeddings(model=model,
                                      deployment=model,
                                      openai_api_key= openai.api_key, 
                                      chunk_size=1)
        st.write("Embeddings created")
        st.write("Creating query result")  

        # # Create a knowledge base using FAISS from the given chunks and embeddings
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)



   






       

        # # Create a knowledge base using FAISS from the given chunks and embeddings  
        # knowledge_base = FAISS.from_texts(chunks, embeddings)

if __name__ == '__main__':
    main()