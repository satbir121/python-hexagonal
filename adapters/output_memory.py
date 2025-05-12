from ports.output import KnowledgeBasePort

class InMemoryKnowledgeBase(KnowledgeBasePort):
    def __init__(self):
        self.qa_pairs = {
            "hi": "Hello there!",
            "how are you?": "I'm just code, but I'm doing well!",
            "bye": "Goodbye!"
        }

    def get_answer(self, question: str) -> str:
        return self.qa_pairs.get(question.lower(), "Sorry, I don't understand that.")