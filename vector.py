from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
import os

embeddings = OllamaEmbeddings(model="mxbai-embed-large")


db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    pdf_folder = "./pdfs"  

    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()

            for i, page in enumerate(pages):
                doc_id = f"{filename}_{i}"
                documents.append(Document(
                    page_content=page.page_content,
                    metadata={"source": filename, "page": i + 1},
                    id=doc_id
                ))
                ids.append(doc_id)

    vector_store = Chroma(
        collection_name="llm_architecture_docs",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    vector_store.add_documents(documents=documents, ids=ids)

else:
    
    vector_store = Chroma(
        collection_name="llm_architecture_docs",
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
