'''
    Необходимо из нескольких длинных строк выбрать
    записи типа mul(X,Y), и просумирровать произведения
    полученных чисел.
'''
import re


def parser(text: str) -> str:
    res = re.findall(r'mul\(\d+,\d+\)', text)
    return res


if __name__ == '__main__':
    res = parser('formwhy()?mul(603,692)({sel}')
    print(res)
