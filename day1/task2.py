with open("./day1/data.txt", "r") as f:
    all_vals = f.read().split()
    left = map(int, all_vals[0::2])
    right = map(int, all_vals[1::2])

    dt_rightcounts = {}
    for i in right:
        if i in dt_rightcounts:
            dt_rightcounts[i] += 1
        else:
            dt_rightcounts[i] = 1

    simscore = 0
    for val in left:
        if val in dt_rightcounts:
            simscore += val * dt_rightcounts[val]

    print(simscore)
