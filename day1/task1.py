with open("./day1/data.txt", "r") as f:
    all_vals = f.read().split()
    left = sorted(map(int, all_vals[0::2]))
    right = sorted(map(int, all_vals[1::2]))
    print(sum((abs(a-b) for a, b in zip(left, right))))
