from knowledge_base import doc_splits
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


#Persisith_path ile DB tarafında belirli ve kalıcı bir base oluşturabilirsin.
#kullanımı için from_documents kütüphanesini incele

embedding= HuggingFaceEmbeddings()

vectorstore = Chroma.from_documents(
    documents=doc_splits,
    embedding=embedding,
    collection_name="rag-chroma",
    persist_directory="./.chroma2"
)


retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma2",
    embedding_function=embedding,
).as_retriever()



