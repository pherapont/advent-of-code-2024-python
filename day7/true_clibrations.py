from copy import deepcopy
from pprint import pprint

# TODO test for parse_data()


def parse_data(file_name:str) -> list[tuple[int, list[int]]]:
    parsed = [] 
    with open(file_name) as f:
        for line in f:
            result, data = line.split(":")
            data_to_arr = data.split()
            parsed.append((int(result.strip()), data_to_arr))
    return parsed


def create_token_tree(nums: list[int], operators: tuple[str]
                      ) -> list[list[str]]:
    if len(nums) == 0: return False
    expressions = [ [str(nums[0])], ]
    for n in nums[1:]:
        tmp = deepcopy(expressions)
        expressions = []
        for item in tmp:
            for op in operators:
                unit = [*item, op, str(n)]
                expressions.append(unit)
    return expressions



def check_calibration(expressions: list[list[int]], res: int) -> bool:
    check = False
    for exp in expressions:
        while len(exp) > 1:
            head = exp[:3]
            tail = exp[3:]
            ans = eval("".join(head))
            exp = [str(ans), *tail]
        tr = int(exp[0])
        if tr == res:
            check = True
    return check


def main(file_name: str) -> int:
    operators = ("+", "*")
    total = 0
    data = parse_data(file_name)
    for res, token in data:
        tree = create_token_tree(token, operators)
        if check_calibration(tree, int(res)):
            total += res
    return total


if __name__ == "__main__":
    res = main("data_input.txt")
    print(res)
