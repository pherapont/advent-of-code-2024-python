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


def divide_updates(
    data: list[list[int]], rules: dict[int, set[int]]
) -> tuple[list[list[int]], list[list[int]]]:
    """
    Проверяем числа стоящие после в каждом update, если они
    встречаются в правиле, то это не корректный update
    """
    correct_update = []
    uncorrect_update = []
    for update in data:
        flag = False
        for pos, num in enumerate(update[:-1]):
            if num in rules:
                for check in update[pos + 1 :]:
                    if check in rules[num]:
                        uncorrect_update.append(update)
                        flag = True
                        break
            if flag:
                break
        if flag:
            continue
        correct_update.append(update)
    return correct_update, uncorrect_update


def transform_updates(row_updates: list[str]) -> list[list[int]]:
    data = [x.split(",") for x in row_updates]
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


def correction_updates(
    uncorrect_updates: list[list[int]], rules: dict[int, set[int]]
) -> list[list[int]]:
    """
    Алгоритм: проходим по записи и каждому числу придаем вес - позицию
    в правилной записи. Вес - сколько элеметов должно стоять перед ней.
    """
    corrected = []
    for update in uncorrect_updates:
        positions = dict(zip(update, [0] * len(update)))
        for pos, num in enumerate(update[:-1]):
            right_elems = []
            counter = 0
            if num not in rules:
                positions[num] = 0
                for elem in update:
                    if elem != num:
                        positions[elem] += 1
                continue
            for elem in update[pos + 1 :]:
                if elem in rules[num]:
                    counter += 1
                else:
                    right_elems.append(elem)
            positions[num] += counter
            for elem in right_elems:
                positions[elem] += counter + 1
        correct_update = sorted(update, key=lambda x: positions[x])
        corrected.append(correct_update)
    return corrected


def get_sum_corrects(data_file: str) -> int:
    row_rules, row_updates = parser_data(data_file)
    updates = transform_updates(row_updates)
    rules = finalize_rules(row_rules)
    correct_updates, _ = divide_updates(updates, rules)
    sum_of_correct = sum([x[len(x) // 2] for x in correct_updates])
    return sum_of_correct


def get_sum_reviseds(data_file: str) -> int:
    row_rules, row_updates = parser_data(data_file)
    updates = transform_updates(row_updates)
    rules = finalize_rules(row_rules)
    _, uncorrect_updates = divide_updates(updates, rules)
    corrected = correction_updates(uncorrect_updates, rules)
    sum_of_corrected = sum([x[len(x) // 2] for x in corrected])
    return sum_of_corrected


if __name__ == "__main__":
    res = get_sum_reviseds("input_data.txt")
    print(res)
