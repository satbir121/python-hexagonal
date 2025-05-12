from dataclasses import dataclass

@dataclass
class Message:
    user_id: str
    text: str

@dataclass
class Response:
    text: str