from typing import Set
from collections import OrderedDict


class MenuPrompt:
    def __init__(self):
        pass

    def choose(self, items: Set[str]) -> str:
        items_dict = OrderedDict()
        for index, item in enumerate(items, 1):
            items_dict[index] = item
        string = '\n'.join(f'{index}: {item}' for index, item in items_dict.items())
        string = '*' * 60 + '\n' + string + '\n' + '*' * 60 + '\n'
        while True:
            try:
                choice = int(input(string))
                if choice not in items_dict.keys():
                    print('Enter correct number!')
                else:
                    return items_dict[choice]
            except:
                print('Enter correct number!')
