"""
Day1: Find all "XMAS" in any directions in the input_data.txt
Day2: Find all "MAS" in shape of X - diagonals in forward or
    back
"""

def search_tails(data: list[str],
                 y0: int, x0: int) -> int:
    ymax = len(data) - 1
    xmax = len(data[0]) - 1
    vectors = {'hf': [(0,1),(0,2),(0,3)],
               'hb': [(0,-1),(0, -2),(0, -3)],
               'vt': [(1,0), (2,0), (3,0)],
               'vd': [(-1,0), (-2,0), (-3,0)],
               'ft': [(1,1), (2,2), (3,3)],
               'fd': [(-1,1), (-2,2), (-3,3)],
               'bt': [(1,-1), (2,-2), (3,-3)],
               'bd': [(-1,-1), (-2,-2), (-3,-3)]
               }
    res = 0

    for vv in vectors.values():
        word = 'X'
        for shift in vv:
            point = list(zip((y0,x0), shift))
            y = sum(point[0])
            x = sum(point[1])
            if y > ymax or y < 0 or x > xmax or x < 0:
                break
            letter = data[y][x]
            word += letter
        if word == 'XMAS':
            res += 1
    return res


def as_in_diagonals(data, y0, x0) -> int:
    ymax = len(data) - 1
    xmax = len(data[0]) - 1
    vectors = {'diag1': [(1, -1), (-1, 1)],
            'diag2': [(1, 1), (-1, -1)]}
    score = 0
    for diags in vectors.values():
        res = set()
        for d in diags:
            point = list(zip(d, (y0, x0)))
            y = sum(point[0])
            x = sum(point[1])
            if y > ymax or y < 0 or x > xmax or x < 0:
                break
            res.add(data[y][x])
        if res == {'S', 'M'}:
            score += 1
    if score == 2:
        return 1
    else:
        return 0


def search_xmas(data: list[str]) -> int:
    res = 0
    for ny, line in enumerate(data):
        for nx, letter in enumerate(line):
            if letter == 'X':
                res += search_tails(data, ny, nx)
    return res


def search_mas(data: list[str]) -> int:
    res = 0
    for ny, line in enumerate(data):
        for nx, letter in enumerate(line):
            if letter == 'A':
                res += as_in_diagonals(data, ny, nx)
    return res


def main(data_file: str) -> int:
    matrix = []
    with open(data_file) as df:
     for line in df:
         matrix.append(line.strip())
    res = search_mas(matrix)
    return res


if __name__ == '__main__':
    res = main("input_data.txt")
    print(res)
