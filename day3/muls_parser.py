'''
    Необходимо из нескольких длинных строк выбрать
    записи типа mul(X,Y), и просумирровать произведения
    полученных чисел.
'''
import re
from itertools import chain


def parser(text: str) -> list[str]:
    res = re.findall(r'mul\(\d+,\d+\)', text)
    return res


def extract_nums_from(mul: str) -> list[int]:
    '''
    Функция извлекает два числа из строки
    типа "mul(213,432)" с числами разной разрядности
    '''
    snums = re.findall(r"\d+", mul)
    return [int(snum) for snum in snums]


def calc_prod(nums):
    res = sum(map(lambda x: x[0] * x[1], nums))
    return res


def main(datafile: str) -> int:
    row_data = []
    with open(datafile, 'r') as df:
        for line in df:
            row_data.append(parser(line))
    data = (extract_nums_from(x) for x in chain.from_iterable(row_data))
    res = calc_prod(data)
    return res


if __name__ == '__main__':
   print(main('data.txt'))
