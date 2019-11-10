from typing import List


class Discipline:
    def __init__(self, name: str):
        self.name = name


class Topic:
    def __init__(self, name: str, discipline: Discipline):
        self.name = name
        self.discipline = discipline


class Question:
    def __init__(
        self, topic: Topic, text: str, answer_options: List[str], correct_answer: str
    ):
        self.topic = topic
        self.text = text
        self.answer_options = answer_options
        self.correct_answer = correct_answer


class QuestionSet:
    def __init__(
        self, questions: List[Question], max_tries_question: int, max_tries_set: int
    ):
        self.questions = questions
        self.max_tries_question = max_tries_question
        self.max_tries_set = max_tries_set


class TestRunner:
    def __init__(self, question_set: QuestionSet):
        self.question_set = question_set
        self.correct_answers_count: int = 0
