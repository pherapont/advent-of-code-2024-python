numbers1 = []
numbers2 = []

def nums_from_file(file_name):
    with open(file_name) as f:
        for line in f:
            n1, n2 = line.split()
            numbers1.append(int(n1.strip()))
            numbers2.append(int(n2.strip()))

def distance():
    numbers1.sort()
    numbers2.sort()
    numbers = [abs(x[0] - x[1]) for x in zip(numbers1, numbers2)]
    return sum(numbers)

def similarity_score():
    res = 0
    for num in numbers1:
        res += num * numbers2.count(num)
    return res

if __name__ == '__main__':
    nums_from_file('input.txt')
    res = similarity_score()
    print(res)