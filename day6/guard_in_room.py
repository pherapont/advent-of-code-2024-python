"""
Сканирование движения охранника по комнате с подсчетом пройденных полей.
Rule of motion: move while achieve "#" than turn right
"""


def data_preparation(file_name: str) -> tuple[list[list[str]], list[int]]: ...


def room_tour(room: list[list[str]], init_pos: list[int]) -> int: ...


def main(file_name: str) -> int:
    data, init_pos = data_preparation(file_name)
    res = room_tour(data, init_pos)
    return res
