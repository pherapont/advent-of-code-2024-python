"""
Метод поиска 'XMAS':
    - чтобы не дублироваться начинаем искать только с 'X'
    - ищем в 8 направлениях
    - прерываем поиск при отклонении от шаблона и при выходе за границу матрицы
    - при нахождении совпадения - просто увеличиваем счетчик
"""
goal = 'XMAS'

def horisont_forward(y: int, x: int, xmax: int) -> list[tuple[int]]:
    res = []
    for i in range(1,4):
        xi = x + i
        if xi > xmax:
            return None
        res.append((y, xi))
    return res

def horisont_back(y: int, x: int) -> list[tuple[int]]:
    res = []
    for i in range(1,4):
        xi = x - i
        if xi < 0:
            return None
        res.append((y, xi))
    return res

def search_tails(data: list[str],
        y: int, x: int, ymax: int, xmax: int) -> int:
    res = 0
    if hf := horisont_forward(y, x, xmax):
        print(hf)
        for i in range(3):
            ind_y = hf[i][0]
            ind_x = hf[i][1]
            print("put", data[ind_y][ind_x])
            print("goal", goal[i+1])
            if data[ind_y][ind_x] == goal[i+1]:
                if i == 2:
                    res += 1
                    print('bingo, res = ', res)
            else: break
    if hb := horisont_back(y, x):
        for i in range(3):
            ind_y = hb[i][0]
            ind_x = hb[i][1]
            print("put", data[ind_y][ind_x])
            print("goal", goal[i+1])
            if data[ind_y][ind_x] == goal[i+1]:
                if i == 2:
                    res += 1
                    print('bingo, res = ', res)
            else: break
    return res
        

def search_xmas(data: list[str]) -> int:
    ymax = len(data) - 1
    xmax = len(data[0]) - 1
    res = 0
    for ny, line in enumerate(data):
        for nx, letter in enumerate(line):
            if letter == 'X':
                print('Search')
                res += search_tails(data, ny, nx, ymax, xmax)
    return res


def main(data_file: str) -> int:
    matrix = []
    with open(data_file) as df:
        for line in df:
            matrix.append(line)
    res = search_xmas(matrix)
    return res
