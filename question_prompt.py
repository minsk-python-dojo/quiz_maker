from typing import List, Set

from menu_prompt import MenuPrompt
from quiz_item import QuizItem
from app_settings import AppSettings
from session_result import SessionResult


class QuestionPrompt(MenuPrompt):
    def __init__(self, questions: List[QuizItem], settings: AppSettings):
        super().__init__()
        self.questions = questions
        self.correct_answer_count = 0
        self.attempt_count = 0
        self.settings = settings

    def choose(self, items: Set[str]) -> str:
        choice = super().choose(items)
        self.attempt_count += 1
        return choice

    def generate_result(self):
        session_result = SessionResult(
            self.correct_answer_count,
            len(self.questions) - self.correct_answer_count,
            self.attempt_count
        ) 
        return session_result

    def ask_question(self):
        for question in self.questions:
            print(question.question)
            question_attempts = 0
            answers: Set[str] = set(question.answers)
            user_answer = self.choose(answers)
            if self.attempt_count >= self.settings.attempts_per_session:
                print('Attempts limit per session is reached. Aborting session.')
                return self.generate_result()
            question_attempts += 1
            question_answered_correctly = user_answer == question.correct_answer
            while not question_answered_correctly:
                if question_attempts >= self.settings.attempts_per_question:
                    print('Attempts limit per question is reached. Showing the next question.')
                    break
                print('Wrong answer. Choose again.')
                user_answer = self.choose(answers)
                if self.attempt_count >= self.settings.attempts_per_session:
                    print('Attempts limit per session is reached. Aborting session.')          
                    return self.generate_result()
                question_answered_correctly = user_answer == question.correct_answer
                question_attempts += 1
            if question_answered_correctly:
                print('Correct answer')
                self.correct_answer_count += 1
        return self.generate_result()
