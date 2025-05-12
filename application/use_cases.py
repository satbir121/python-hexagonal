from ports.input import ChatInputPort
from domain.chatbot import Chatbot
from domain.models import Message, Response

class ChatService(ChatInputPort):
    def __init__(self, chatbot: Chatbot):
        self.chatbot = chatbot

    def handle_message(self, message: Message) -> Response:
        answer = self.chatbot.get_response(message.text)
        return Response(text=answer)