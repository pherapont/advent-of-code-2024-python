from pprint import pprint
from collections import namedtuple

DiskElem = namedtuple("DiskElem", ["eid", "esize"])

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
            ) -> list[dict[str, int]]:
    disk_structure = []
    for index, elem in enumerate(disk_desc):
        if index % 2:
            field = {"gap": elem, "el": 0, "elems": []}
            disk_structure.append(field)
        else:
            d_e = DiskElem(eid=index // 2, esize=elem)
            field = {"gap": 0, "el": elem, "elems": [d_e]}
            disk_structure.append(field)
    return disk_structure


def defragment_disk_by_files(
        dstruct: list[dict[str, int]]
            ) -> list[dict[str, int]]:
    for i in range(len(dstruct) - 1, 0, -1):
        if ds_el := dstruct[i]["el"]:
            for j in range(i):
                if dstruct[j]["gap"] >= ds_el:
                    dstruct[j]["gap"] -= ds_el
                    dstruct[j]["el"] += ds_el
                    dstruct[i]["gap"] += ds_el
                    dstruct[i]["el"] -= ds_el
                    dstruct[j]["elems"].append(dstruct[i]["elems"].pop(0))
                    break
        else:
            continue
    return dstruct


def file_map(defr_disk: list[dict[str, int]]) -> tuple[int]:
    disk_map: list[int] = []
    gap_id = -1
    for block in defr_disk:
        if block["el"]:
            for el in block["elems"]:
                for i in range(el.esize):
                    disk_map.append(el.eid)
            for j in range(block["gap"]):
                disk_map.append(-1)
        else:
            for j in range(block["gap"]):
                disk_map.append(-1)
    return tuple(disk_map)


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
    d_s = get_disk_structure(data)
    d_d = defragment_disk_by_files(d_s)
    d_m = file_map(d_d)
    return get_check_sum(d_m)


if __name__ == "__main__":
    res = main("data_main_input.txt")
    print(res)
