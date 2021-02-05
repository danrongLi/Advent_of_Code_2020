def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        # return f.readlines()
        return [int(line[:-1]) for line in f.readlines()]

def part1(vals: list) -> int:
    for val in vals:
        if (2020 - val) in vals:
            return (2020 - val) * val

def part2(vals: list) -> int:
    for i in range(len(vals)):
        for j in range(i, len(vals)):
            if (2020 - vals[i] - vals[j]) in vals:
                return vals[i] * vals[j] *  (2020 - vals[i] - vals[j])


if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
# jk