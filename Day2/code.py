def readfile():
    data = []
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        raw_data = f.readlines()
        for item in raw_data:
            txt = item.split()
            nums = txt[0].split("-")
            data.append((int(nums[0]), int(nums[1]), txt[1][:-1], txt[2]))
    return data


def part1(data):
    valid_passwords = 0
    for item in data:
        minimum = item[0]
        maximum = item[1]
        count = item[-1].count(item[-2])
        if (count<=maximum and count>=minimum):
            valid_passwords+=1
    return valid_passwords

def part2(data):
    valid_passwords = 0
    for item in data:
        has_position = item[0]
        not_position = item[1]
        if ((item[-1][has_position-1] == item[-2]) and (item[-1][not_position-1] != item[-2])):
            valid_passwords += 1
        elif ((item[-1][has_position-1] != item[-2]) and (item[-1][not_position-1] == item[-2])):
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))


