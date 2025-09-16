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
        print("Begin search")
        for shift in vv:
            point = list(zip((y0,x0), shift))
            y = sum(point[0])
            x = sum(point[1])
            print(f"y = {y}, x = {x}")
            if y > ymax or y < 0 or x > xmax or x < 0:
                print("BREAK")
                print(f"xmax = {xmax}, ymax = {ymax}")
                break
            letter = data[y][x]
            word += letter
            print(word)
        if word == 'XMAS':
            res += 1
    return res


def search_xmas(data: list[str]) -> int:
    res = 0
    for ny, line in enumerate(data):
        for nx, letter in enumerate(line):
            if letter == 'X':
                res += search_tails(data, ny, nx)
    return res


def main(data_file: str) -> int:
    matrix = []
    with open(data_file) as df:
     for line in df:
         matrix.append(line.strip())
    res = search_xmas(matrix)
    return res


if __name__ == '__main__':
    res = main("input_data.txt")
    print(res)
