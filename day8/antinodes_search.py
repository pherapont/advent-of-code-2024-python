def search_anitnodes(map: list[list[str]]) -> int:
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
