from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from prompt_temp import llm


store= {}

def get_session_history(session_id= str)->BaseChatMessageHistory:
    if session_id not in store:
        store[session_id]= InMemoryChatMessageHistory()
    return store[session_id]

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful RAG assistant. Answer all questions to the best of your ability. "),
        MessagesPlaceholder(variable_name="messages")
    ]
)



chain= prompt | llm

config= {"configurable" : {"session_id" : "123"}}

with_message_history= RunnableWithMessageHistory(chain, get_session_history)
