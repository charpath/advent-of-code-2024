import re

with open("./day3/data.txt") as f:
    print(contents := f.read())
    print(re.findall(r"mul\(\d+,\d+\)", "abcmul(11,22)h"))
    matches = re.findall(r"mul\(\d+,\d+\)", contents)

    multsum = 0
    for match in matches:
        halves = match.split(",")
        halves[0] = halves[0][4:]
        halves[1] = halves[1][:-1]
        halves = list(map(int, halves))
        multsum += halves[0] * halves[1]
    print(multsum)
