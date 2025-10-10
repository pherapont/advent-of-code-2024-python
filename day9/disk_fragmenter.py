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
                disk_map.append(i / 2)
    return tuple(disk_map)


def defragment_disk(disk_map_data: tuple[int]) -> tuple[int]:
    disk_map = list(disk_map_data)
    direct_counter = 0
    back_counter = len(disk_map) - 1
    while direct_counter != back_counter:
        if disk_map[direct_counter] == -1:
            if disk_map[back_counter] == -1:
                back_counter -= 1
                continue
            else:
                disk_map[direct_counter] = disk_map[back_counter]
                back_counter -= 1
                direct_counter += 1
        else:
            direct_counter += 1
            continue
    return tuple(disk_map[:direct_counter])

    return ()
