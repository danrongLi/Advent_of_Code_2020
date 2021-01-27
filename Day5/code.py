# F/L: lower half
def readfile():
    result = list()
    with open("input.txt", "r") as f:
        for lines in f.read().split():
            result.append(lines)
    return result

def findseat(code):
    row_low = 0
    row_high = 127
    for fb in code[0:7]:
        if fb == "F":
            row_high = (row_high+row_low-1)/2
            row_low = row_low
        elif fb == "B":
            row_low = (row_high+row_low+1)/2
            row_high = row_high

    col_low = 0
    col_high = 7
    for rl in code[7::]:
        if rl == "L":
            col_high = (col_high+col_low-1)/2
            col_low = col_low
        elif rl == "R":
            col_low = (col_high+col_low+1)/2
            col_high = col_high

    return int(row_low), int(col_low)

def find_max(data):
    current_max = 0
    for code in data:
        current_row, current_col = findseat(code)
        current_id = 8*current_row + current_col
        if current_id > current_max:
            current_max = current_id
    return current_max

def get_all(data):
    all_passengers = []
    for code in data:
        current_row, current_col = findseat(code)
        current_id = 8 * current_row + current_col
        all_passengers.append(current_id)
    for ids in all_passengers:
        if (ids+2 in all_passengers) and (ids+1 not in all_passengers):
            print(ids+1)
    return True

if __name__ == "__main__":
    data = readfile()
    print(data)
    print(find_max(data))
    print(get_all(data))