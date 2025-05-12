class Chatbot:
    def __init__(self, qa_knowledge_base):
        self.qa_knowledge_base = qa_knowledge_base

    def get_response(self, message_text: str) -> str:
        return self.qa_knowledge_base.get_answer(message_text)