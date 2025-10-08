from pprint import pprint


def get_nodes_coordinates(map: list[list[str]], node: str) -> list[tuple[int]]:
    res: list[tuple[int]] = []
    for nline, line in enumerate(map):
        for nx, x in enumerate(line):
            if x == node:
                res.append((nline, nx))
    return res


def search_antinodes(
    nodes: list[tuple[int]], field_size: tuple[int]
) -> set[tuple[int]]:
    antinodes: set[tuple[int]] = set()
    while len(nodes) > 1:
        chief = nodes.pop(0)
        for node in nodes:
            diff_positive = [x[1] - x[0] for x in zip(chief, node)]
            diff_negative = [x[0] - x[1] for x in zip(chief, node)]
            # antinode1 = chief + diff_negative
            # antinode2 = node + diff_negative
            while chief[0] in range(field_size[0]) and chief[1] in range(field_size[1]):
                antinode = (chief[0], chief[1])
                antinodes.add(antinode)
                tmp = [sum(x) for x in zip(chief, diff_negative)]
                chief = tmp
            while node[0] in range(field_size[0]) and node[1] in range(field_size[1]):
                antinode = (node[0], node[1])
                antinodes.add(antinode)
                tmp = [sum(x) for x in zip(node, diff_positive)]
                node = tmp
    print(antinodes)
    return antinodes


def get_data_from_file(file_name: str) -> list[list[str]]:
    map: list[list[str]] = []
    with open(file_name) as f:
        for line in f:
            arr = list(line.strip())
            map.append(arr)
    return map


def main(file_name: str) -> int:
    map = get_data_from_file(file_name)
    all_antinodes: set[tuple[int]] = set()
    field_size = (len(map), len(map[0]))
    nodes: set[str] = set()
    for line in map:
        for node in line:
            if node != ".":
                nodes.add(node)
    for node in nodes:
        coordinates = get_nodes_coordinates(map, node)
        antinodes_coords = search_antinodes(coordinates, field_size)
        all_antinodes.update(antinodes_coords)
    return len(all_antinodes)


if __name__ == "__main__":
    res = main("data_main_test.txt")
    pprint(res)
