"""
Метод поиска 'XMAS':
    - чтобы не дублироваться начинаем искать только с 'X'
    - ищем в 8 направлениях
    - прерываем поиск при отклонении от шаблона и при выходе за границу матрицы
    - при нахождении совпадения - просто увеличиваем счетчик
"""
from pprint import pprint

goal = 'XMAS'

def search_xmas(data: list[str]) -> int:
    pprint(data)
    for nx, line in enumerate(data):
        for ny, letter in enumerate(line):
            if letter == 'X':
                print(f"'X' in string {nx} in column {ny}")
    return 0


def main(data_file: str) -> int:
    matrix = []
    with open(data_file) as df:
        for line in df:
            matrix.append(line)
    res = search_xmas(matrix)
    return res
