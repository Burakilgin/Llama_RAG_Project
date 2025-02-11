import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from prompt_temp import llm
from vector_store import retriever
from prompt_temp import rag_chain
from memory import with_message_history

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    mode: str

class RAGApplication:

    def __init__(self, retriever, rag_chain):
        self.with_message_history = with_message_history
        self.retriever = retriever
        self.rag_chain = rag_chain

    def run_rag(self, question):

        documents = self.retriever.invoke(question)
        doc_texts = "\n".join([doc.page_content for doc in documents])
        response = self.rag_chain.invoke({"question": question, "documents": doc_texts})

        return response

    def run_chat(self, question, session_id="123"):

        response = self.with_message_history.invoke(
            [
                HumanMessage(content=question)
            ],
            config={"configurable": {"session_id": session_id}},
        )

        return response


rag_application = RAGApplication(retriever, rag_chain)


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    if request.mode.lower() == "rag":
        response = rag_application.run_rag(request.question)
    elif request.mode.lower() == "chat":
        response = rag_application.run_chat(request.question)

    return {"question": request.question, "answer": response}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
