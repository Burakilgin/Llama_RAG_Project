from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from knowledge_base import doc_splits
from langchain_community.vectorstores import Chroma

load_dotenv()

#Persisith_path ile DB tarafında belirli ve kalıcı bir base oluşturabilirsin.
#kullanımı için from_documents kütüphanesini incele


vectorstore = Chroma.from_documents(
    documents=doc_splits,
    embedding=OpenAIEmbeddings(),
    collection_name="rag-chroma",
    persist_directory="./.chroma1"
)


retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma1",
    embedding_function=OpenAIEmbeddings(),
).as_retriever()



