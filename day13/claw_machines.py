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


def get_cheapest_coordinates(
        a: tuple[int, int],
        b: tuple[int, int],
        location: tuple[int, int]
        ) -> int:
    """
    1) Находим сочетания Ax, Bx, которые приведут к цели по x
    2) Находим сочетания Ay, By, которые приведут к цели по y
    3) Находим одинаковые пары сочетаний.
    Победит пара, имеюшая наименьшеую цену.
    """
    wins: list[tuple[int, int]] = []
    ax_steps, rest = divmod(location[0], a[0])
    bx_steps = 0
    if rest:
        ax_steps += 1
    works = True
    while ax_steps and works:
        works = False
        x_length = ax_steps * a[0] + bx_steps * b[0]
        while x_length <= location[0]:
            if x_length == location[0]:
                wins.append((ax_steps, bx_steps))
            else:
                continue
        if ax_steps:
            works = True
        ax_steps -= 1
    res_arr = [(x * 3, y) for x, y in wins]
    res = min(res_arr)
    return (res[0] // 3, res[1])
    

if __name__ == '__main__':
    a = (2, 2)
    b = (3, 3)
    location = (10, 10)
    get_cheapest_coordinates(a, b, location)
