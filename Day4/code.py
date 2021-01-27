import re

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

    return part1_valid


def part2(part1_ans):

    pattern = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*"
    }

    return sum((all((re.fullmatch(pattern[key], passport[key]) for key in passport)) for passport in part1_ans))


if __name__ == "__main__":
    data = readfile()
    part1_ans = part1(data)
    print(len(part1_ans))
    print(part2(part1_ans))