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


def search_antinodes(nodes: list[tuple[int]], bounds: tuple[int]) -> list[tuple[int]]:
    while len(nodes) > 1:
        chief = nodes.pop(0)
        for node in nodes:
            vector = zip(chief, node)
            diff_positive = [x[1] - x[0] for x in zip(chief, node)]
            diff_negative = [x[0] - x[1] for x in zip(chief, node)]
            print(f"chief {chief}")
            print(f"node {node}")
            print(f"vector {list(vector)}")
            print(f"d-n {diff_negative}")
            print(f"d-p {diff_positive}")
