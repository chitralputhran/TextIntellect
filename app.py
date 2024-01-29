# Imports
import streamlit as st 
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

# Constants
PAGE_TITLE = "TextIntellect AI"
PAGE_ICON = "🔎"
OPENAI_API_KEY_PROMPT = 'OpenAI API Key'
FILE_UPLOAD_PROMPT = "Upload your Text file here"
FILE_UPLOAD_TYPE = ".txt"

def setup_ui():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, initial_sidebar_state="collapsed")
    st.header("",divider='blue')
    st.title(f"{PAGE_ICON} :blue[_{PAGE_TITLE}_] | Text File Search")
    st.header("",divider='blue')

def api_key_check(openai_api_key):
    if not openai_api_key.startswith('sk-'):
        st.info("Please add your OpenAI API key in the sidebar to continue.")
        st.stop()

def load_instructions():
    with st.sidebar:  
      st.divider()   
      st.write('*Your Research AI Adventure begins with a Text file.*')
      st.caption('''**That's why I'd love for you to upload a Text file. 
                 Once we have your file, we'll understand it and start exploring it.
                  Then, we'll work together to answer whatever questions you have.
                  Sounds fun, right?**''')
      st.divider()

def handle_file_upload(user_file, openai_api_key):
    if user_file is None:
        return
    documents = [user_file.read().decode()]
    splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=200, chunk_overlap=30)
    doc_splits = splitter.create_documents(documents)

    # Create the embeddings for the text file
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)
    chroma_db = Chroma.from_documents(doc_splits, embedding_function)

    # Train the model
    llm = ChatOpenAI(temperature=0,openai_api_key=openai_api_key)
    solution = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=chroma_db.as_retriever())

    st.success("Text file embeddings were successfully inserted into VectorDB")

    return solution

def ask_question(user_file, solution):
    if user_file is None:
        return
    st.divider()
    question = st.text_input('Please enter your question:', placeholder = "Which year was Marty transported to?", disabled=not user_file)

    if question:
        result = solution.run(question)
        st.info(result)
        st.divider()

def main():
    # Setup the UI
    setup_ui()

    # Get OpenAI API key
    openai_api_key = st.sidebar.text_input(OPENAI_API_KEY_PROMPT, type='password')

    # Check the API key
    api_key_check(openai_api_key)

    # Show user instructions
    load_instructions()

    # File uploader
    user_file = st.file_uploader(FILE_UPLOAD_PROMPT, type=FILE_UPLOAD_TYPE)

    # Handle the file upload
    solution = handle_file_upload(user_file, openai_api_key)

    # Ask the question
    ask_question(user_file, solution)

if __name__ == "__main__":
    main()