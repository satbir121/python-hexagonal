from fastapi import FastAPI
from application.use_cases import ChatService
from domain.models import Message
from domain.chatbot import Chatbot
from adapters.output_memory import InMemoryKnowledgeBase

app = FastAPI()

knowledge_base = InMemoryKnowledgeBase()
chatbot = Chatbot(knowledge_base)
chat_service = ChatService(chatbot)

@app.post("/chat")
def chat(user_id: str, text: str):
    message = Message(user_id=user_id, text=text)
    response = chat_service.handle_message(message)
    return {"response": response.text}