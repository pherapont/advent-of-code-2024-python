def get_data_from_file(file_name:str) -> tuple[int]:
    data = []
    data_str: str
    with open(file_name) as f:
        data_str = f.readline()
    for i in data_str.strip():
        data.append(int(i))
    return tuple(data)


def get_disk_map(disk_desc: tuple[int]) -> tuple[int]:
    map: list[int] = []
    gap_id = -1
    for i, num in enumerate(disk_desc):
        for j in range(num):
            if i % 2:
                map.append(gap_id)
            else:
                map.append(i / 2)
    return tuple(map)
