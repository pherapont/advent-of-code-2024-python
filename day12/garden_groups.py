directs = ((0, 1), (0, -1), (1, 0), (-1, 0))
all_visited: list[tuple[int]] = []


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
        struct_region.append(subline) 
    for el in region_vector[1:]:
        y, x = el
        if y == line_num and x == subline[-1][1] + 1:
            subline.append(el)
        else:
            struct_region.append(subline)
            subline = [el]
            line_num = y
    return len(struct_region) * 2


def region_cost(region: tuple[tuple[int]]) -> int:
    first_half_cost = bounds_count(region)
    # second - транспонировать матрицу и отдать в функуию bounds_count()
    

def explore_region(garden: tuple[tuple[str]], init_point: tuple[int]) -> tuple[tuple[int]]:
    y_size = len(garden)
    x_size = len(garden[0])
    region = [init_point]
    visited: list[tuple[int]] = [init_point]
    work_points: list[tuple[int]] = [init_point]
    plant = garden[init_point[0]][init_point[1]]
    while len(work_points) > 0:
        for point in work_points:
            py, px = point
            for direct in directs:
                ny, nx = [sum(x) for x in zip((py, px), direct)]
                in_garden = ny in range(y_size) and nx in range(x_size)
                if in_garden and garden[ny][nx] == plant and (ny, nx) not in visited:
                    visited.append((ny, nx))
                    work_points.append((ny, nx))
                    region.append((ny, nx))
            work_points.remove(point)
            all_visited.append(visited)
    return tuple(sorted(region))


def garden_regions(garden: tuple[tuple[str]]) -> int:
    common_cost = 0
    for y, line in enumerate(garden):
        for x, plant in enumerate(line):
            if (y, x) in visited:
                continue
            for direct in directs:
                ny, nx = [sum(x) for x in zip((y, x), direct)]
                if garden[ny][nx] == plant and (ny, nx) not in visited:
                    visited.append((y, x))
                    region = explore_region(garden, (y, x))
                    cost = region_cost(region)
                    common_cost += cost
                    break
    return common_cost
