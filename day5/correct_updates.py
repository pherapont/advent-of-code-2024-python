"""
Из файла с данными необходимо выделить все корректные строки
и найти сумму их средних членов.
"""
def parser_data(data_file: str) -> tuple[list[str], list[str]]:
    with open(data_file) as df:
        updates_flag = False
        rules = []
        updates = []
        for line in df:
            line = line.strip()
            if len(line) == 0:
                updates_flag = True
                continue
            if not updates_flag:
                rules.append(line)
            else:
                updates.append(line)
    return rules, updates


def filter_bad_updates(data: list[list[int]],
                       rules: dict[int, set[int]]) -> list[list[int]]:
    """
    Проверяем числа стоящие после в каждом update, если они
    встречаются в правиле, то это не корректный update
    """
    correct_update = []
    for update in data:
        flag = False
        for pos, num in enumerate(update[:-1]):
            if num in rules:
                for check in update[pos+1:]:
                    if check in rules[num]:
                        flag = True
                        break
            if flag: break
        if flag: continue    
        correct_update.append(update)
    return correct_update


def transform_updates(row_updates: list[str]) -> list[list[int]]:
    data = [x.split(',') for x in row_updates]
    res = []
    for chunk in data:
        res.append([int(x) for x in chunk])
    return res


def finalize_rules(row_rules: list[str]) -> dict[int, set[int]]:
    """
    В правило (множество) каждого числа, включаем числа, которые
    должны передшествовать этому числу
    """
    rules = {}
    for line in row_rules:
        rule = line.split("|")
        rule_key = int(rule[1])
        rule_value = int(rule[0])
        if rule_key not in rules:
            rules[rule_key] = {rule_value}
        else:
            rules[rule_key].add(rule_value)
    return rules


def main(data_file: str) -> int:
    row_rules, row_updates = parser_data(data_file)
    updates = transform_updates(row_updates)
    rules = finalize_rules(row_rules)
    correct_updates = filter_bad_updates(updates, rules)
    return sum([x[len(x) // 2] for x in correct_updates])

if __name__ == '__main__':
    res = main("input_data.txt")
    print(res)
