from copy import deepcopy


def parse_data(file_name:str) -> list[tuple[str, list[str]]]:
    parsed = [] 
    with open(file_name) as f:
        for line in f:
            result, data = line.split(":")
            data_to_arr = data.split()
            parsed.append((result.strip(), data_to_arr))
    return parsed


def create_token_tree(nums: list[str], operators: tuple[str]
                      ) -> list[list[str]]:
    if len(nums) == 0: return False
    expressions = [ [nums[0]], ]
    for n in nums[1:]:
        tmp = deepcopy(expressions)
        expressions = []
        for item in tmp:
            for op in operators:
                unit = [*item, op, n]
                expressions.append(unit)
    return expressions



def check_calibration(expressions: list[list[str]], res: str) -> bool:
    check = False
    for exp in expressions:
        while len(exp) > 1:
            head = exp[:3]
            tail = exp[3:]
            if head[1] == "||":
                ans = head[0] + head[2]
                exp = [ans, *tail]
            else:
                ans = eval("".join(head))
                exp = [str(ans), *tail]
        tr = exp[0]
        if tr == res:
            check = True
    return check


def main(file_name: str) -> int:
    operators = ("+", "*", "||")
    total = 0
    data = parse_data(file_name)
    n = 1
    for res, token in data:
        print(f"Line {n}")
        n += 1
        tree = create_token_tree(token, operators)
        if check_calibration(tree, res):
            total += int(res)
    return total


if __name__ == "__main__":
    res = main("data_input.txt")
    print(res)
