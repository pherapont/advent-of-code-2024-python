from collections import namedtuple

Machine = namedtuple("Machine", ["a", "b", "loc"])


def get_cheapest_way(a: tuple[int],
                     b: tuple[int],
                     location: tuple[int]
                     ) -> int:
    """
    1) Находим сочетания Ax, Bx, которые приведут к цели по x
    2) Находим сочетания Ay, By, которые приведут к цели по y
    3) Находим одинаковые пары сочетаний.
    Победит пара, имеюшая наименьшеую цену.
    """
    res_x = get_result_steps(a[0], b[0], location[0])
    res_y = get_result_steps(a[1], b[1], location[1])
    wins: set[tuple[int, int]] = res_x & res_y
    normed_wins = {win: win[0] * 3 + win[1] for win in wins}
    if normed_wins:
        win = min(normed_wins, key=normed_wins.get)
        return normed_wins[win]
    else:
        return 0


def get_cheapest_math(a: tuple[int],
                     b: tuple[int],
                     loc: tuple[int]
                     ) -> int:
    """
    Количество шагов каждой кнопкой находим решая систему 2 уравнений
    с 2 неизвестными. Это позволит решить задачу с огромными числами.
    """
    res = 0
    descr: int = b[0] * a[1] - b[1] * a[0]
    if descr == 0:
        return get_cheapest_way(a, b, loc)
    res_b, rest = divmod((loc[0] * a[1] - loc[1] * a[0]), descr)
    if rest:
        return 0
    res_a, rest = divmod((loc[1] - res_b * b[1]), a[1]) 
    if rest:
        return 0
    return res


def get_result_steps(
        ax: int,
        bx: int,
        locx: int
        ) -> set[tuple[int, int]]:
    """
    Начинаем с достижение цели используя только а-кнопку, постепенно 
    уменьшаем ее роль, одновременно увеличевая роль б-кнопки. Так перебираем
    все варианты достижения цели по одной координате.
    Возвращаем список всех сочетаний, достигающих цели, 
    Победителя выберет основная функция.
    """
    wins: set[tuple[int, int]] = set()
    ax_steps, rest = divmod(locx, ax)
    bx_steps = 0
    if rest:
        ax_steps += 1
    works = True
    while ax_steps and works:
        bx_steps = 0
        works = False
        x_length = 0
        while x_length <= locx:
            x_length = ax_steps * ax + bx_steps * bx
            if x_length == locx:
                wins.add((ax_steps, bx_steps))
                break
            else:
                bx_steps += 1
        if ax_steps:
            works = True
            ax_steps -= 1
    return wins
    

def get_file_data(file_name: str) -> list[Machine]:
    res = []
    a: tuple[int, int]
    b: tuple[int, int]
    loc: tuple[int, int]
    with open(file_name) as data_file:
        for line in data_file:
            a: tuple[int, int]
            b: tuple[int, int]
            loc: tuple[int, int]
            if line.strip():
                name, coord = line.split(":")
                if name.startswith("Button"):
                    n = name.split()[1].strip()
                    coords = [x.split("+")[1] for x in coord.split(",")]
                    if n == "A":
                        a = tuple(int(x) for x in coords)
                    else:
                        b = tuple(int(x) for x in coords)
                else:
                    coords = [x.split("=")[1] for x in coord.split(",")]
                    loc = tuple(int(x) for x in coords)
            else:
                res.append(Machine(a, b, loc))
        res.append(Machine(a, b, loc))
    return res    


def main(file_name: str) ->int:
    res = 0
    data: list[Machine] = get_file_data(file_name)
    for m in data:
        price = get_cheapest_way(m.a, m.b, m.loc)
        res += price
    return res


if __name__ == '__main__':
    res = main("main_data.txt")
    print(res)