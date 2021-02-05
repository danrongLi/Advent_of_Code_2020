def readfile():
    result = list()
    with open("input.txt", "r") as f:
        for lines in f.read().split("\n\n"):
            result.append(lines.replace("\n", ""))
    return result


def get_questions(line):
    return len(set(line))


def get_sum(data):
    count_sum = 0
    for line in data:
        count_sum += get_questions(line)


if __name__ == "__main__":
    data = readfile()
    print(data)
    print(get_questions(data))
