from dotenv import load_dotenv
import os
import streamlit as st


# set page config, header, and file uploader

def main():
    load_dotenv()

    st.set_page_config(
        page_title="Microsoft Demo",
        page_icon="🎯",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.header("Talk to your PDF 💬")
    pdf = st.file_uploader("Upload PDF 📑")


if __name__ == '__main__':
    main()