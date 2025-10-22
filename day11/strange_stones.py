def get_data_from_file(file_name: str) -> tuple[str]:
    res = []
    with open(file_name) as f:
        line = f.readline()
        res = line.split()
    return tuple(res)


def transform_stones(stones: tuple[str], blinks: int) -> list[str]:
    """
    1) If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    2) If the stone is engraved with a number that has an even number of digits,
        it is replaced by two stones.
        The left half of the digits are engraved on the new left stone,
        and the right half of the digits are engraved on the new right stone.
        (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    3) If none of the other rules apply, the stone is replaced by a new stone; 
        the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    new_stones = list(stones)
    for bl in range(blinks):
        prev_stones = new_stones.copy()
        new_stones = []
        for stone in prev_stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) and not len(stone) % 2:
                mid = len(stone) // 2
                first = stone[:mid]
                new_stones.append(first)
                # отбрасывание передних незначачих нулей
                last = str(int(stone[mid:]))
                new_stones.append(last)
            else:
                new_stone = str(int(stone) * 2024)
                new_stones.append(new_stone)
    return new_stones

def transform_one_stone(stn: str, blinks: int) -> list[str]:
    new_stones = [stn]
    for bl in range(blinks):
        prev_stones = new_stones.copy()
        new_stones = []
        for stone in prev_stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) and not len(stone) % 2:
                mid = len(stone) // 2
                first = stone[:mid]
                new_stones.append(first)
                # отбрасывание передних незначачих нулей
                last = str(int(stone[mid:]))
                new_stones.append(last)
            else:
                new_stone = str(int(stone) * 2024)
                new_stones.append(new_stone)
    return new_stones


# программа уходит в бесконечнось по памяти или по времени
# идея - кэшировать на 2-ом и 3-ем уровнях так как один элемент всегда приведет к одному результату
def main(file_name: str, blink_count: int) -> int:
    data = get_data_from_file(file_name)
    res = 0
    for stone in data:
        print(f"{stone=}")
        data1 = transform_one_stone(stone, 25)
        for elem in data1:
            print(f"{elem=}")
            data2 = transform_one_stone(elem, 25)
            for el in data2:
                res += len(transform_one_stone(el, 25))
    return res


if __name__ == "__main__":
    res = main("main_data.txt", 75)
    # res = main("test_data.txt", 25)
    print(res)