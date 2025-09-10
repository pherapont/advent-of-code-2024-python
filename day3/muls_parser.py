'''
    Необходимо из нескольких длинных строк выбрать
    записи типа mul(X,Y), и просумирровать произведения
    полученных чисел.
'''
import re


def parser(text: str) -> list[str]:
    res = re.findall(r'mul\(\d+,\d+\)', text)
    return res

def extract_nums_from(mul: str) -> list(int):
    '''
    Функция извлекает два числа из строки
    типа "mul(213,432)" с числами разной разрядности
    '''
    ...


def main(datafile: str) -> int:
    data = []
    with open(datafile, 'r') as df:
        for line in df:
            data.append(parser(line))

    print(data)
    return 0

if __name__ == '__main__':
    main('data.txt')
