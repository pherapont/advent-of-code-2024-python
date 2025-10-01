"""
Сканирование движения охранника по комнате
с подсчетом пройденных полей.
Rule of motion: move while achieve "#" than turn right
"""

from itertools import cycle
from pprint import pprint


def data_preparation(file_name: str) -> tuple[list[list[int]], list[int]]:
    with open(file_name) as f:
        struct_room = []
        init_pos: list[int]  # first - row(y), second - column(x)
        for y, line in enumerate(f):
            line = line.strip()
            struct_line = []
            for x, ch in enumerate(line):
                if ch == "#":
                    struct_line.append(1)
                elif ch == "^":
                    init_pos = [y, x]
                    struct_line.append(0)
                else:
                    struct_line.append(0)
            struct_room.append(struct_line)
    return struct_room, init_pos


def room_tour(room: list[list[int]], init_pos: list[int]) -> int:
    right_bound = len(room[0])
    down_bound = len(room)
    pos = dict(zip(("y", "x"), init_pos))
    directions = cycle(["up", "right", "down", "left"])
    dir_rules = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    dir = next(directions)
    visits = {(pos["y"], pos["x"])}
    while True:
        step = dir_rules[dir]
        next_pos = (r + q for (r, q) in zip(pos.values(), step))
        np = dict(zip(("y", "x"), next_pos))
        if np["x"] not in range(right_bound) or np["y"] not in range(down_bound):
            break
        elif room[np["y"]][np["x"]] == 1:
            dir = next(directions)
        else:
            pos = np
            visits.add((np["y"], np["x"]))
    pprint(visits)
    return len(visits)


def is_cycle(
    room: list[list[int]],
    way: set[tuple[int, int]],
    init_pos: list[int],
    obstruction: list[int],
) -> bool:
    # Проблема: в этой функции надо снова организовывать обход комнаты
    # можно попробывать выделить обход в отдельную функцию
    check_points: list[tuple[int, int], str] = []


def main(file_name: str) -> int:
    data, init_pos = data_preparation(file_name)
    res = room_tour(data, init_pos)
    return res


if __name__ == "__main__":
    res = main("data_input.txt")
    print(res)
