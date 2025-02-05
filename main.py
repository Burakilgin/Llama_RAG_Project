from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage
from prompt_temp import llm
from vector_store import retriever
from prompt_temp import rag_chain
from memory import with_message_history,config
from langchain.chains import ConversationChain

class RAGApplication:

    def __init__(self, retriever, rag_chain):
        self.with_message_history = with_message_history
        self.retriever = retriever
        self.rag_chain = rag_chain


    def run(self, question):

        if ans=="y" or ans== "Y":
            documents = self.retriever.invoke(question)
            doc_texts = "\\n".join([doc.page_content for doc in documents])
            response = self.rag_chain.invoke({"question": question, "documents": doc_texts})
            return response

        elif ans =="n" or ans== "N":
            documents = self.retriever.invoke(question)
            doc_texts = "\\n".join([doc.page_content for doc in documents])
            response = self.with_message_history.invoke(
                [
                    HumanMessage(content=question)
                ],
                config= config
            )
            return response


    def chat(self,user_input):
        response_chat = self.conversation_chain.run(user_input)
        return response_chat

memory = ConversationBufferMemory()
conversation_chain = ConversationChain(llm=llm, memory=memory)

rag_application = RAGApplication(retriever, rag_chain)


if __name__=="__main__":

    ans= input("What do you want to do? Y: RAG SYSTEM N: MEMORY SYSTEM")

    while True:

        if ans== "Y" or ans=="y":
            question = input("What's your RAG question?\n")
            response = rag_application.run(question)
            print("Question:", question)
            print("Answer:", response)

        elif ans== "N" or "n":
            question= input("What's your memory question?\n")
            response =  rag_application.run(question)
            print("Answer: ", response.content)

        elif ans == "chat":
            user_input = input("You: ")
            response = rag_application.chat(question)
            print("AI:", response)

