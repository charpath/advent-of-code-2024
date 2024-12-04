def check_horizontal(arr: list[list[str]], line: int, col: int) -> int:
    ln = arr[line]
    out = 0
    try:
        if ln[col+1] == 'M' and ln[col+2] == 'A' and ln[col+3] == 'S':
            out += 1
    except IndexError:
        pass
    try:
        if (col >= 3 and ln[col-1] == 'M'
                and ln[col-2] == 'A' and ln[col-3] == 'S'):
            out += 1
    except IndexError:
        pass
    return out


def check_vertical(arr: list[list[str]], line: int, col: int) -> int:
    out = 0
    try:
        if (arr[line+1][col] == 'M'
                and arr[line+2][col] == 'A' and arr[line+3][col] == 'S'):
            out += 1
    except IndexError:
        pass
    try:
        if (line >= 3 and arr[line-1][col] == 'M'
                and arr[line-2][col] == 'A' and arr[line-3][col] == 'S'):
            out += 1
    except IndexError:
        pass
    return out


def check_diag(arr: list[list[str]], line: int, col: int) -> int:
    out = 0
    try:
        if (arr[line+1][col+1] == 'M'
                and arr[line+2][col+2] == 'A' and arr[line+3][col+3] == 'S'):
            out += 1
    except IndexError:
        pass
    try:
        if (col >= 3 and arr[line+1][col-1] == 'M'
                and arr[line+2][col-2] == 'A' and arr[line+3][col-3] == 'S'):
            out += 1
    except IndexError:
        pass
    try:
        if (line >= 3 and col >= 3 and arr[line-1][col-1] == 'M'
                and arr[line-2][col-2] == 'A' and arr[line-3][col-3] == 'S'):
            out += 1
    except IndexError:
        pass
    try:
        if (line >= 3 and arr[line-1][col+1] == 'M'
                and arr[line-2][col+2] == 'A' and arr[line-3][col+3] == 'S'):
            out += 1
    except IndexError:
        pass
    return out


with open("./day4/data.txt") as f:
    arr = []
    for line in f:
        arr.append(list(line.strip()))
    # print(arr)
    XMAS_ct = 0

    for line in range(len(arr)):
        for col in range(len(arr[line])):
            if arr[line][col] == "X":
                XMAS_ct += (check_horizontal(arr, line, col)
                            + check_vertical(arr, line, col)
                            + check_diag(arr, line, col))
    print(XMAS_ct)
