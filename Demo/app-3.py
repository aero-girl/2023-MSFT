from dotenv import load_dotenv
import os
import openai
import streamlit as st


# set page config, header, and file uploader

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

if __name__ == '__main__':
    main()