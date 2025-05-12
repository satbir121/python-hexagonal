from abc import ABC, abstractmethod

class KnowledgeBasePort(ABC):
    @abstractmethod
    def get_answer(self, question: str) -> str:
        pass