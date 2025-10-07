from pprint import pprint


def check_nodes(map: list[list[str]]) -> int:
    res: set[list[int]] = {}
    node: str = ""
    out_search: set[str] = {}
    current_nodes: list[tuple[int]] = []

    for ny, y in enumerate(map):
        for nx, x in enumerate(y):
            if x != "." and x not in out_search and not node:
                node = x
                current_nodes.append((y, x))
            elif x == node:
                current_nodes.append((y, x))


def search_antinodes(nodes: list[tuple[int]], field_size: tuple[int]) -> list[tuple[int]]:
    antinodes: list[tuple[int]] = []
    while len(nodes) > 1:
        chief = nodes.pop(0)
        for node in nodes:
            vector = zip(chief, node)
            diff_positive = [x[1] - x[0] for x in zip(chief, node)]
            diff_negative = [x[0] - x[1] for x in zip(chief, node)]
            #antinode1 = chief + diff_negative
            #antinode2 = node + diff_negative
            ans = ([sum(x) for x in zip(chief, diff_negative)], [sum(x) for x in zip(node, diff_positive)])
            for an in ans:
                an0 = int(an[0])
                an1 = int(an[1])
                if (an0 in range(field_size[0]) and
                        an1 in range(field_size[1])):
                    antinode = (an0, an1)
                    antinodes.append(antinode)
    pprint(antinodes)
    return antinodes
