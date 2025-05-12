from abc import ABC, abstractmethod
from domain.models import Message

class ChatInputPort(ABC):
    @abstractmethod
    def handle_message(self, message: Message):
        pass