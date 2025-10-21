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
                last = stone[mid:]
                new_stones.append(last)
            else:
                new_stone = str(int(stone) * 2024)
                new_stones.append(new_stone)
    return new_stones