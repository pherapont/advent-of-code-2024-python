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
    wins: set[tuple[int, int]] = set()
    res_x = get_result_steps(a[0], b[0], location[0])
    res_y = get_result_steps(a[1], b[1], location[1])
    print(f"{res_x=}")
    print(f"{res_y=}")


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
    

if __name__ == '__main__':
    a = (2, 2)
    b = (3, 3)
    location = (10, 11)
    res = get_cheapest_way(a, b, location)
    print(res)