from vector_store import retriever
from prompt_temp import rag_chain


class RAGApplication:

    def __init__(self, retriever, rag_chain):
        self.retriever = retriever
        self.rag_chain = rag_chain


    def run(self, question):
        documents = self.retriever.invoke(question)

        doc_texts = "\\n".join([doc.page_content for doc in documents])

        response = self.rag_chain.invoke({"question": question, "documents": doc_texts})
        return response


rag_application = RAGApplication(retriever, rag_chain)

if __name__=="__main__":
    question = input("What's your question?\n")
    response = rag_application.run(question)
    print("Question:", question)
    print("Answer:", response)