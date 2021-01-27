def readfile():
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        raw_data = f.readlines()
        data_wo_dash = [item[:-1] for item in raw_data]
        return data_wo_dash

def part1(data, dx, dy):
    length = len(data)
    width = len(data[0])
    x = y = 0
    tree = 0
    while (y + dy) < length:
        x = (x + dx) % width
        y += dy
        if data[y][x] == "#":
            tree += 1
    return tree

def part2(data):
    tree11 = part1(data,1,1)
    tree31 = part1(data,3,1)
    tree51 = part1(data,5,1)
    tree71 = part1(data,7,1)
    tree12 = part1(data,1,2)
    return tree11 * tree31 * tree51 * tree71 * tree12

if __name__ == "__main__":
    data = readfile()
    part1_trees = part1(data, 3, 1)
    print(part1_trees)
    part2_trees = part2(data)
    print(part2_trees)