class Application:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def run(self):
        print(f'config path: {self.data_path}')
