from typing import List, Set

from menu_prompt import MenuPrompt
from quiz_item import QuizItem


class QuestionPrompt(MenuPrompt):
    def __init__(self, questions: List[QuizItem]):
        super().__init__()
        self.questions = questions
        self.correct_answer_count = 0
        self.attempt_count = 0

    def choose(self, items: Set[str]) -> str:
        choice = super().choose(items)
        self.attempt_count += 1
        return choice

  
    def ask_question(self):
        for question in self.questions:
            print(question.question)
            answers: Set[str] = set(question.answers)
            user_answer = self.choose(answers)

            while user_answer != question.correct_answer:
                print('Wrong answer. Choose again.')
                user_answer = self.choose(answers)
            print('Correct answer')
            self.correct_answer_count += 1
        
