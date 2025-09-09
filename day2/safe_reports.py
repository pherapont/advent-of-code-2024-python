'''
На входе из файла получаем список строк.
1. Преобразовать строки в списки int.
2. Проверить списки на соответствие тз:
    а) Числа в списке строго возрастают или строго убывают.
    б) Разность соседних чисел на больше 3

Оба эти действия выделяются в отдельные функции и хорошо тестируютс
'''

def get_nums(line: str) -> list[int]:
    return [int(num) for num in line.split()]

def check_report(report: list[int]) -> bool:
    diff = [x[1] - x[0] for x in zip(report[:], report[1:])]
    print (diff)
    return True

if __name__ == '__main__':
    check_report([1, 4, 5, 2])
