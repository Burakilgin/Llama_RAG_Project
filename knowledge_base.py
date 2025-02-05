from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


source = [
"D:\\Burak_Files\\AiForce\\Rag_Calismalari\\ASC2012-Cenk_Hoca_Makale.pdf"
]

docs = [PyPDFLoader(url).load() for url in source]
docs_list = [item for sublist in docs for item in sublist]


text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)

doc_splits = text_splitter.split_documents(docs_list)