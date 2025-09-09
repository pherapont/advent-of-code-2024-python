'''
На входе из файла получаем список строк.
1. Преобразовать строки в списки int.
2. Проверить списки на соответствие тз:
    а) Числа в списке строго возрастают или строго убывают.
    б) Разность соседних чисел на больше 3

Оба эти действия выделяются в отдельные функции и хорошо тестируютс
How many reports are safe
Part2:
    We can remove one bad level and report become safe
'''


def get_nums(line: str) -> list[int]:
    return [int(num) for num in line.split()]


def check_report(report: list[int]) -> bool:
    diff = [x[1] - x[0] for x in zip(report[:], report[1:])]
    return all(3 >= x > 0 for x in diff) or all(0 > x >= -3 for x in diff)


def check_light_report(report: list[int]) -> bool:
    for i, number in enumerate(report):
        light_report = report[:i] + report[i+1:]
        if check_report(light_report):
            return True
    return False


def main(filename: str):
    res = 0
    with open(filename, 'r') as f:
        for line in f:
            numbers = get_nums(line)
            if check_report(numbers):
                res += 1
            else:
                if check_light_report(numbers):
                    res += 1
    return res


if __name__ == '__main__':
    res = main('data.txt')
    print(res)
