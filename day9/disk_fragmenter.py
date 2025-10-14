from pprint import pprint
from collections import namedtuple

DiskElem = namedtuple("DiskElem", ["elems", "gap_size"])

def get_data_from_file(file_name: str) -> tuple[int]:
    data = []
    data_str: str
    with open(file_name) as f:
        data_str = f.readline()
    for i in data_str.strip():
        data.append(int(i))
    return tuple(data)


def get_disk_structure(
        disk_desc: tuple[int]
            ) -> tuple[tuple[str, int]]:
    row_disk_structure = []
    for index, elem in enumerate(disk_desc):
        d_e: DiskElem
        if index % 2:
            d_e = DiskElem(elems=[], gap_size=elem)
        else:
            # elements pack in list of tuple(id, size)
            d_e = DiskElem(elems=[(index//2, elem)], gap_size=0)
        row_disk_structure.append(d_e)
    return tuple(row_disk_structure)


#TODO: освоить дебаггер для python
def defragment_disk_by_files(
        disk_structure: tuple[tuple[int]]
            ) -> tuple[tuple[int]]:
    dds = list(disk_structure)  #disk defragment structure
    for i in range(len(disk_structure) - 1, 0, -1):
        if not dds[i].elems:
            continue
        else:
            for j in range(len(disk_structure)):
                print(dds[i].elems)
                if(dds[j].gap_size >= dds[i].elems[0][1]):
                    new_el = dds[j].elems.append(dds[i].elems[0])
                    l_gap = dds[j].gap_size - dds[i].elems[0][1]
                    r_gap = dds[i].gap_size + dds[i].elems[0][1] 
                    r_el = dds[i].elems[1:]
                    dds[j] = DiskElem(elems=new_el, gap_size=l_gap)
                    dds[i] = DiskElem(elems=r_el, gap_size=r_gap)
                    break
    return dds


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
                disk_map[cursor_back] = -1
                cursor_back -= 1
                if cursor < cursor_back:
                    cursor += 1
        else:
            cursor += 1
            continue
    return tuple(disk_map)


def get_check_sum(disk: tuple[int]) -> int:
    res = 0
    for pos, block_id in enumerate(disk):
        if block_id == -1:
            continue
        res += pos * block_id
    return res


def main(file_name: str) -> int:
    data = get_data_from_file(file_name)
    d_m = get_disk_map(data)
    d_d = defragment_disk(d_m)
    return get_check_sum(d_d)


if __name__ == "__main__":
    disk_desc = (1, 2, 3, 4, 5)
    res = get_disk_structure(disk_desc)
    dds = defragment_disk_by_files(res)
    print("----------RES---------")
    pprint(res)
    print("----------DDS---------")
    pprint(dds)
