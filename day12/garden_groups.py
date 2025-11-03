directs = ((0, 1), (0, -1), (1, 0), (-1, 0))

visited: list[tuple[int]] = []


def bounds_count(region_vector: tuple[tuple[int]]) -> int:
    """
    границы по направлению = сумма всех подстрок * 2
    подстрока = целая строка без разрывов или участки строк между разрывами
    соответственно надо подсчитать по вертикали и горизонтали
    """
    struct_region = []
    init_el = region_vector[0]
    subline = [init_el]
    line_num: int = init_el[0]
    if len(region_vector) == 1:
        struct_region.append(init_el) 
    for el in region_vector[1:]:
        y, x = el
        if y == line_num and x == subline[-1][1] + 1:
            subline.append(el)
        else:
            struct_region.append(subline)
            subline = [el]
            line_num = y
    struct_region.append(subline)
    print(struct_region)
    return len(struct_region) * 2


def region_cost(region: tuple[tuple[int]]) -> int:
    first_half_cost = bounds_count(region)
    # second - транспонировать матрицу и отдать в функуию bounds_count()
    

def explore_region(garden: tuple[tuple[str]],
                init_point: tuple[int],
                plant: str
                ) -> tuple[tuple[int]]:
    y_size = len(garden)
    x_size = len(garden[0])
    region = [init_point]
    work_points: list[tuple[int]] = [init_point]
    visited.append(init_point)
    while len(work_points) > 0:
        for point in work_points:
            for direct in directs:
                ny, nx = [sum(x) for x in zip(point, direct)]
                in_garden = ny in range(y_size) and nx in range(x_size)
                if in_garden and garden[ny][nx] == plant and (ny, nx) not in visited:
                    visited.append((ny, nx))
                    work_points.append((ny, nx))
                    region.append((ny, nx))
            work_points.remove(point)
    return tuple(sorted(region))


def explore_garden(garden: tuple[tuple[str]]) -> int:
    common_cost = 0
    for y, line in enumerate(garden):
        for x, plant in enumerate(line):
            if (y, x) in visited:
                continue
            region = explore_region(garden, (y, x), plant)
            cost = region_cost(region)
            common_cost += cost
    return common_cost
