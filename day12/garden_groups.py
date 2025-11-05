directs = ((0, 1), (0, -1), (1, 0), (-1, 0))

def get_struct_region(region_vector: list[tuple[int]]
                      ) -> list[list[tuple[int]]]:
    struct_region = []
    init_el = region_vector[0]
    subline = [init_el]
    line_num: int = init_el[0]
    for el in region_vector[1:]:
        y, x = el
        if y == line_num and x == subline[-1][1] + 1:
            subline.append(el)
        else:
            struct_region.append(subline)
            subline = [el]
            line_num = y
    struct_region.append(subline)
    return struct_region


def bounds_count(region_vector: list[tuple[int]]) -> int:
    struct_region = get_struct_region(region_vector)
    return len(struct_region) * 2


def sides_count(region_vector: list[tuple[int]]) -> int:
    struct_region = get_struct_region(region_vector)
    res = 0
    # dict l1 =left of 1; r2 right bound of 2 point
    sides: dict[str, list[int]] = {}
    for subline in struct_region:
        left_bound_key = f"l{subline[0][1]}"
        right_bound_key = f"r{subline[-1][1]}"
        for key in (left_bound_key, right_bound_key):
            if key in sides:
                sides[key].append(subline[0][0])
            else:
                sides[key] = [subline[0][0]]
    # Считаем стороны. В ячейке словаря может быть несколько сторон
    print(sides)
    for _, value in sides:
        for index, el in enumerate(value):
            if index > 0 and el == value[index - 1] + 1:
                continue
            else:
                res += 1
        res += 1
    return res


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


def get_garden(file_name: str) -> tuple[tuple[str]]:
    garden = []
    with open(file_name) as  fi:
        for line in fi:
            garden.append(tuple(line.strip()))
    return tuple(garden)


def main(file_name:str) -> int:
    garden = get_garden(file_name)
    res = explore_garden(garden)
    return res


if __name__ == "__main__":
    res = main("main_input.txt")
    print(res)
