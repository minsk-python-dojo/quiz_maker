from dataclasses import dataclass


@dataclass
class QuizItem:
    discipline: str
    topic: str
    question: str
