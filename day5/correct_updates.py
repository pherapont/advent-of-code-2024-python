"""
Из файла с данными необходимо выделить все корректные строки
и найти сумму их средних членов.
"""
def parser_data(data_file: str) -> tuple[list[str]]:
    with open(data_file) as df:
        updates_flag = False
        rules = []
        updates = []
        for line in df:
            line = line.strip()
            print(line)
            if len(line) == 0:
                print('Empty line')
                updates_flag = True
                continue
            if not updates_flag:
                rules.append(line)
                print(f"rules = {rules}")
            else:
                updates.append(line)
                print(f"updates = {updates}")
    return rules, updates


def main(data_file: str) -> int:
    rules, updates = parser_data(data_file)
            
