directs = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bounds_count(region_vector: list[tuple[int]]) -> int:
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
    return len(struct_region) * 2


def region_cost(region: list[tuple[int]]) -> int:
    row_bounds_count = bounds_count(region)
    rotate_region = sorted([tuple(reversed(x)) for x in region])
    column_bounds_count = bounds_count(rotate_region)
    len_region = len(region)
    print(f"{len_region=}")
    print(f"{row_bounds_count=}")
    print(f"{column_bounds_count=}")
    return (row_bounds_count + column_bounds_count) * len(region)
    

def explore_region(garden: tuple[tuple[str]],
                visited: list[tuple[int]],
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
    visited: list[tuple[int]] = []
    common_cost = 0
    for y, line in enumerate(garden):
        for x, plant in enumerate(line):
            if (y, x) in visited:
                continue
            region = explore_region(garden, visited, (y, x), plant)
            cost = region_cost(region)
            common_cost += cost
            print(f"{plant=} - {cost=}")
    return common_cost
