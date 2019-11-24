import os
import json
from typing import List, Set
from menu_prompt import MenuPrompt
from quiz_item import QuizItem


class Application:
    def __init__(self, data_dir_path: str, data_file_name: str):
        self.data_dir_path: str = data_dir_path
        self.data_file_name: str = data_file_name
        self.quiz_data: List[QuizItem] = []
        self.menu_prompt = MenuPrompt()

    def read_quiz_data(self):
        data_file_path = os.path.join(self.data_dir_path, self.data_file_name)
        with open(data_file_path, "r") as f:
            quiz_raw_data = json.load(f)
        quiz_items = [QuizItem.from_dict(quiz_item) for quiz_item in quiz_raw_data]
        return quiz_items

    def run(self):
        self.quiz_data = self.read_quiz_data()
        disciplines: Set[str] = {quiz_item.discipline for quiz_item in self.quiz_data}
        chosen_discipline: str = self.menu_prompt.choose(disciplines)
        topics: List[str] = [
            quiz_item.topic
            for quiz_item in self.quiz_data
            if quiz_item.discipline == chosen_discipline
        ]
        chosen_topic: str = self.menu_prompt.choose(topics)
        questions: List[QuizItem] = [
            quiz_item for quiz_item in self.quiz_data if quiz_item.topic == chosen_topic
        ]
        print(questions)

    def parse_disciplines(self):
        disciplines_data_path = os.path.join(self.data_path, "disciplines.json")
        f = open(disciplines_data_path, "r")
        disciplines_data = json.load(f)
        f.close()
        return disciplines_data
