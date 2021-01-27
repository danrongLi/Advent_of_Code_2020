def readfile():
    result = list()
    with open("input.txt", "r") as f:
        for lines in f.read()[:-1].split("\n\n"):
            result.append(dict(d.split(":") for d in lines.split()))
    return result

def part1(data):
    required_keys = ['eyr', 'hgt', 'pid', 'ecl', 'byr', 'hcl', 'iyr']

    def if_valid_keys(passport):
        if_list = []
        for keys in required_keys:
            if_list.append(keys in passport)
        return all(if_list)

    part1_valid = []
    for passport in data:
        if if_valid_keys(passport):
            part1_valid.append(passport)

    return len(part1_valid)


if __name__ == "__main__":
    data = readfile()
    part1_ans = part1(data)
    print(part1_ans)