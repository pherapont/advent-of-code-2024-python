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


def finalize_rules(row_rules: list[str]) -> dict[str, set[str]]:
    rules = {}
    for line in row_rules:
        rule = line.split("|")
        if rule[1] not in rules:
            rules[rule[1]] = {rule[0]}
        else:
            rules[rule[1]].add(rule[0])
    return rules


def main(data_file: str) -> int:
    row_rules, updates = parser_data(data_file)
    rules = finalize_rules(row_rules)
    return 0
