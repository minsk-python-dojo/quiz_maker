import os
import json


class Application:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def run(self):
        print(f'config path: {self.data_path}')

    def parse_disciplines(self):
        disciplines_data_path = os.path.join(self.data_path, "disciplines.json")
        f = open(disciplines_data_path, 'r')
        disciplines_data = json.load(f)
        f.close()
        return disciplines_data


        
    
            


