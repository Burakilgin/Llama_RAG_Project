from langchain_community.vectorstores import SKLearnVectorStore
from langchain_openai import OpenAIEmbeddings
from knowledge_base import doc_splits
from dotenv import load_dotenv

load_dotenv()

vectorstore = SKLearnVectorStore.from_documents(
    documents=doc_splits,
    embedding=OpenAIEmbeddings(openai_api_key="YOUR_API_KEY"),
)

retriever = vectorstore.as_retriever(k=4)