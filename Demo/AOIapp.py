# Author: Gavita Regunath
from dotenv import load_dotenv
import streamlit as st # import streamlit
from streamlit_extras.add_vertical_space import add_vertical_space
import openai
from langchain.llms import AzureOpenAI
from langchain.vectorstores import OpenSearchVectorSearch
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from langchain import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain

import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from PIL import Image


# Set page config
st.set_page_config(page_title = "🗣 Talk to your PDF Demo")

# Sidebar contents
with st.sidebar:
    st.title("💬 Q&A on your enterprise data")
    st.markdown(  """
        ### Steps:
        1. Upload PDF File
        2. Perform Q&A
    **Note : This is using Azure OpenAI**

    ## Your DATA is your MOAT
        """)
    add_vertical_space(3)
    st.write('Made with ❤️ by [Gavita Regunath](https://www.linkedin.com/in/gavitaregunath/)')


def main():
    load_dotenv('.env') # load environment variables

    # Configure Azure OpenAI Service API
    os.environ["OPENAI_API_TYPE"] = "azure"
    os.environ["OPENAI_API_VERSION"] = "2023-08-01-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY") # set OpenAI API key
    openai.api_base = os.getenv("OPENAI_API_BASE") # set OpenAI Base URL

    # Define models
    model = "text-embedding-ada-002"
    completion_model = "gpt-35-turbo"

    image = Image.open('Images\HighResIconWithTextLong.png')
    st.image(image, use_column_width = 'auto')    
    st.markdown('Using SOTA LLMs, Vector Stores, and Question Answering Chains to talk to your PDFs')
    st.header("Talk to your PDF 💬")

    # Upload PDF file
    # pdf = st.file_uploader("Choose a file", type = ["pdf"])

# # Write a function to extract the text from a PDF file
#     if pdf is not None:
#         pdf_reader = PdfReader(pdf)
#         text = "" # empty string to store the text
#         for page in pdf_reader.pages: # for each page in the pdf
#             text += page.extract_text() # concatenating all the text from the pages

        # st.write(text) # display the text on the streamlit app  

    loader = PyPDFLoader('docs/2023 Microsoft Dublin.pdf')
    pages = loader.load_and_split()
   
    # Load documents 
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = OpenAIEmbeddings(model=model, deployment=model, openai_api_key= openai.api_key, chunk_size=1)
    st.write("embeddings created")   

    with st.spinner("It's indexing..."):
        knowledge_base = FAISS.from_documents(docs, embeddings)
    st.success("Embeddings done.", icon="✅")

    # get user question
    question = st.text_input("Ask your question here:") # get user question

    if question: # if user question is not empty
        # search for similar documents
        docs_db = knowledge_base.similarity_search(question)
        
        # Define the LLM model
        llm = AzureOpenAI(deployment_name=completion_model, model_name=completion_model, temperature=0.5, max_tokens=2000) 
        chain = load_qa_chain(llm, chain_type="stuff")

        response = chain({"input_documents": docs_db, "question": question, "language": "English", "existing_answer" : ""}, return_only_outputs=True)
        st.write(response) # display the response on the streamlit app
      

# Run the app 
if __name__ == '__main__':
    main()