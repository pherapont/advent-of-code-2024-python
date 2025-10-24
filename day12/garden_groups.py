directs = ((0, 1), (0, -1), (1, 0), (-1, 0))
all_visited: list[tuple[int]] = []


def region_cost(region: tuple[tuple[int]]) -> int:
    ...

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
