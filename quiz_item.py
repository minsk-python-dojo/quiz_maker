from dataclasses import dataclass
from typing import List

@dataclass
class QuizItem:
    discipline: str
    topic: str
    question: str
    answers: List[str]
    correct_answer: str
    
    @classmethod
    def from_dict(cls, raw_quiz_item: dict):
        discipline = raw_quiz_item.get("discipline", "Unknown discipline")
        topic = raw_quiz_item.get("topic", "Unknown topic")
        question = raw_quiz_item.get("question", "Unknown question")
        answers = raw_quiz_item.get("answers", [])
        correct_answer = raw_quiz_item.get("correct_answer", "Unknown correct answer")
        
        quiz_item = cls(discipline, topic, question, answers, correct_answer)
        
        return quiz_item