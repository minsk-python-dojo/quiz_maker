#!/usr/bin/env python3
import os
import sys

import quiz

from app import Application


def main(data_path: str) -> None:
    quiz_app = Application(data_path)
    quiz_app.run()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error! At least 1 argument expected. Aborting.')
        sys.exit(1)      
    data_path = sys.argv[1]
    if not os.path.exists(data_path):
        print(f'Error! {data_path} is not a valid path. Aborting.')
        sys.exit(1)
    main(data_path)
    