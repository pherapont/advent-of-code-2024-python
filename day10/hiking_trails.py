def get_trail_score(t_map: list[list[int]], t_head: tuple[int]) -> int:
    """
        Задача: найти в окружении текущих точек точки со значением на 1 больше.
        Записать все пути от t_head до новой точки.
        Вообще путь полностью записывать не нужно, можно только корректную последнюю точку.
        Если у точки нет соседей +1, то удалить путь до этой точки из списка.
    """
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    h_bound = len(t_map[0])
    v_bound = len(t_map)
    trails = [t_head]
    for point in range(1, 10):
        tmp_trails = trails.copy()
        trails = []
        for last in tmp_trails:
            for step in steps:
                next = list(sum(x) for x in zip(last, step))
                y, x = next
                if y in range (v_bound) and x in range(h_bound) and t_map[y][x] == point:
                    trails.append((y, x))
        print(f"{point=}--{trails=}")
    return len(trails)


if __name__ == "__main__":
    from data_simple_test import t_map
    get_trail_score(t_map, (0,3))
