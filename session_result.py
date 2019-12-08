from dataclasses import dataclass


@dataclass
class SessionResult:
    correct_answer_count: int
    incorrect_answer_count: int
    attempt_count: int

    def show(self):
        print(f'Session results:\nCorrectly answered: {self.correct_answer_count}\nIncorrectly answered: {self.incorrect_answer_count}\nAttempts: {self.attempt_count}')