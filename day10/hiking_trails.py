def get_trail_map(file_name: str) -> list[list[int]]:
    t_map = []
    with open(file_name) as f:
        for line in f:
            t_map.append([int(i) for i in list(line.strip())])
    return t_map


def get_trail_score(t_map: list[list[int]], t_head: tuple[int]) -> int:
    """
        Задача: найти в окружении текущих точек точки со значением на 1 больше.
        Записать все пути от t_head до новой точки.
        !! Ошибка: надо искать не количество уникальных путей, а количество достижимых точек 9.
        Поэтому в спсок включаем только уникальные точки.
        Вообще путь полностью записывать не нужно, можно только корректную последнюю точку.
        Если у точки нет соседей +1, то удалить путь до этой точки из списка.
    """
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    h_bound = len(t_map[0])
    v_bound = len(t_map)
    trails = {t_head}
    for point in range(1, 10):
        tmp_trails = trails.copy()
        trails = set()
        for last in tmp_trails:
            for step in steps:
                next = list(sum(x) for x in zip(last, step))
                y, x = next
                if y in range (v_bound) and x in range(h_bound) and t_map[y][x] == point:
                    trails.add((y, x))
    return len(trails)

def main(file_name: str) -> int:
    t_map = get_trail_map(file_name)
    res = 0
    for y, line in enumerate(t_map):
        for x, elem in enumerate(line):
            if elem == 0:
                score = get_trail_score(t_map, (y, x))
                res += score
    return res

if __name__ == "__main__":
    res = main("data_main_input.txt")
    print(res)