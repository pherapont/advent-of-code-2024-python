def get_data_from_file(file_name: str) -> tuple[int]:
    data = []
    data_str: str
    with open(file_name) as f:
        data_str = f.readline()
    for i in data_str.strip():
        data.append(int(i))
    return tuple(data)


def get_disk_map(disk_desc: tuple[int]) -> tuple[int]:
    disk_map: list[int] = []
    gap_id = -1
    for i, num in enumerate(disk_desc):
        for j in range(num):
            if i % 2:
                disk_map.append(gap_id)
            else:
                disk_map.append(i // 2)
    return tuple(disk_map)


def defragment_disk(disk_map_data: tuple[int]) -> tuple[int]:
    disk_map = list(disk_map_data)
    cursor = 0
    cursor_back = len(disk_map) - 1
    while cursor < cursor_back:
        if disk_map[cursor] == -1:
            if disk_map[cursor_back] == -1:
                cursor_back -= 1
            else:
                disk_map[cursor] = disk_map[cursor_back]
                cursor_back -= 1
                if cursor < cursor_back:
                    cursor += 1
        else:
            cursor += 1
            continue
    res = disk_map[:cursor] if disk_map[cursor] == -1 else disk_map[: cursor + 1]
    return tuple(res)


def get_check_sum(disk: tuple[int]) -> int:
    res = 0
    for pos, block_id in enumerate(disk):
        res += pos * block_id
    return res


def main(file_name: str) -> int:
    data = get_data_from_file(file_name)
    d_m = get_disk_map(data)
    d_d = defragment_disk(d_m)
    return get_check_sum(d_d)


if __name__ == "__main__":
    res = main("data_main_input.txt")
    print(res)
