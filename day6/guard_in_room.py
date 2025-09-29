"""
Сканирование движения охранника по комнате
с подсчетом пройденных полей.
Rule of motion: move while achieve "#" than turn right
"""


def data_preparation(file_name: str
                     ) -> tuple[list[list[int]], list[int]]:
    with open(file_name) as f:
        struct_room = []
        init_pos: list[int]
        for y, line in enumerate(f):
            line = line.strip()
            struct_line = []
            for x, ch in enumerate(line):
                if ch == "#":
                    struct_line.append(1)
                elif ch == "^":
                    init_pos = [x, y]
                    struct_line.append(0)
                else:
                    struct_line.append(0)
            struct_room.append(struct_line)
    return struct_room, init_pos


def room_tour(room: list[list[int]], init_pos: list[int]
              ) -> int:
    right_bound = len(room[0])
    down_bound = len(room)
    pos = dict(zip(("y", "x"), (init_pos)))
    directions = ["up", "right", "down", "left"]
    dir_rules = {"up": (-1, 0), "right": (0, 1),
                 "down": (1, 0), "left": (0, -1)}
    dir = directions[0]
    while right_bound > pos['x'] >= 0 and down_bound >= pos['y'] >= 0:
        step = dir_rules[dir]
        next_pos = (r + q for (r, q) in zip(pos.values(), step))
        next_pos = dict(zip(('y', 'x'), next_pos))
        if room[np['y']][np['x']] == 1:
            ...
        #TODO make generator from itertools.cycle(directions)


def main(file_name: str) -> int:
    data, init_pos = data_preparation(file_name)
    res = room_tour(data, init_pos)
    return res
