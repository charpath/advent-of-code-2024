import re

with open("./day3/data.txt") as f:
    reg = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
    print(re.findall(reg, "abcmul(11,22)do()hhjesdon't()ajw"))
    matches = re.findall(reg, f.read())
    print(matches)

    multsum = 0
    do_op = True
    for match in matches:
        if match == "don't()":
            do_op = False
        elif match == "do()":
            do_op = True
        elif do_op:
            halves = match.split(",")
            halves[0] = halves[0][4:]
            halves[1] = halves[1][:-1]
            halves = list(map(int, halves))
            multsum += halves[0] * halves[1]
    print(multsum)
