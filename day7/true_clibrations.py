from copy import deepcopy

# TODO test for parse_data()


def parse_data(file_name:str) -> list[tuple[int, list[int]]:
    parsed = [] 
    with open(file_name) as f:
        for line in f:
            result, data = line.split(":")
            data_to_arr = data.split()
            parsed.append(result.strip(), data_to_arr)
    return parsed


def check_calibration(nums: list[int], res: int) -> bool:
    expressions = [ [str(nums[0])], ]
    operators = ("+", "*")
    for n in nums[1:]:
        tmp = deepcopy(expressions)
        expressions = []
        for item in tmp:
            for op in operators:
                unit = [*item, op, str(n)]
                expressions.append(unit)
    for exp in expressions:
        token = "".join(exp)
        tr = eval(token)
        if tr == res:
            return True
    return False
