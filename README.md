# 🔎 TextIntellect AI | Text File Search

## Description
TextIntellect AI is a web application designed to enhance text file comprehension by enabling users to query the contents of uploaded text files interactively. The application processes the file, converts the text into embeddings using Natural Language Processing (NLP) techniques, and stores the embeddings in ChromaDB. Users can then ask questions about the contents, and the system will generate answers based on the processed data.

This application is a type of Retrieval-Augmented Generation (RAG) system, where the retrieval of relevant text segments is augmented with generative capabilities.

## Features
- **Upload Text Files:** Users can upload text files of any format.
- **Text Embedding:** Text contents are converted into embeddings, which capture semantic meaning for advanced processing.
- **Question and Answer System:** Users can ask specific questions about the uploaded text, and the app will generate relevant answers.
- **ChromaDB Integration:** Efficient storage and retrieval of text embeddings with ChromaDB.
- **Streamlit UI:** User-friendly interface built using Streamlit.
- **LangChain Backend:** Backend powered by the LangChain framework for handling embedding and query logic.

## How It Works
- **Upload a Text File:** Simply upload any text-based file.
- **Text Processing:** The application processes the contents by creating vector embeddings.
- **Ask Questions:** Once embeddings are generated, users can interactively ask questions related to the file content.
- **Retrieve Answers:** The application uses the embeddings to retrieve the most relevant information and generate responses to the user's queries.  

## Screenshot 
![Screen_1](https://github.com/chitralputhran/TextIntellect/assets/31520972/70b4fd84-2183-48f7-a43a-bca9de8db987)

## Technologies Used
- **Streamlit:** For building an intuitive user interface.
- **LangChain:** As the backbone for managing text embeddings and retrieval.
- **ChromaDB:** For embedding storage and fast, efficient querying.
- **Python:** Core programming language.

## Installation

### Setup
Clone the repository:
```
git clone https://github.com/chitralputhran/TextIntellect.git
```

Install dependencies:
```
pip install -r requirements.txt
```

### Running the Application
Navigate to the application directory and run:
```
streamlit run app.py
```

## Usage
1. Start the application.
2. Upload the text file through the Streamlit interface.
3. Wait for the embedding process to complete.

