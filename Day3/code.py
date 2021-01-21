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

if __name__ == "__main__":
    data = readfile()
    part1_trees = part1(data, 3, 1)
    print(part1_trees)