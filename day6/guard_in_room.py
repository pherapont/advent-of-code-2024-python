"""
Сканирование движения охранника по комнате с подсчетом пройденных полей.
Rule of motion: move while achieve "#" than turn right
"""

def data_preparation(file_name: str) -> list[list[str]]:
    ...


def get_init_pos(room_wit_guard: list[list[str]]) -> list[int]:
    ...


def room_tour(room: list[list[str]], init_pos: list[int]) -> int:
    ...


def main(file_name: str) -> int:
    data = data_preparation(file_name)
    init_pos = get_init_pos(data)
    res = room_tour(data, init_pos)
    return res
