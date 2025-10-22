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

def main(file_name: str, blink_count: int) -> int:
    data = get_data_from_file(file_name)
    t_s = transform_stones(data, blink_count)
    return len(t_s)

if __name__ == "__main__":
    res = main("main_data.txt", 25)
    print(res)