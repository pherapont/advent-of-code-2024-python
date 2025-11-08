def get_cheapest_way(a: tuple[int],
                     b: tuple[int],
                     location: tuple[int]
                     ) -> int:
    """
    Перебирае все достижимые точки для наибольшего количества шагов
    Со второго шага проверяем добавочные шаги другого типа пока
    сканирование не уйдет дальше цеши.
    """
    wins: list[tuple[int, int]] = []
    steps_a = max(location[0] // a[0], location[1] // a[1])
    steps_b = max(location[0] // b[0], location[1] // b[1])
    print(steps_a)
    print(steps_b)


if __name__ == '__main__':
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    get_cheapest_way(a, b, location)
