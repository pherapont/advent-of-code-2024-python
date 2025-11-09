def get_initial_steps_count(machine: tuple[int, int],
                     location: tuple[int, int]
                     ) -> int:
    """
    Функция оценивает какое кол. шагов нужно для достижения или перелета
    конечным автоматом цели в одиночку.
    Правда эта оценка очень неточная, т.к. вклад каждой координаты в 
    достижение цели неравномерный и , возможно, отставший автомат, по другой
    координате внесет решающий вклад.
    Нужно или вносить какие-то весовые характеристики в координаты или тупо
    перебирать все варианты.
    """
    x, tail = divmod(location[0], machine[0])
    if tail:
        x += 1
    y, tail = divmod(location[1], machine[1])
    if tail:
        y += 1
    return x + y


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
    init_cost_a = get_initial_steps_count(a, location) * 3
    init_cost_b = get_initial_steps_count(b, location)
    print(f"{init_cost_a=}")
    print(f"{init_cost_b=}")

if __name__ == '__main__':
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    get_cheapest_way(a, b, location)
