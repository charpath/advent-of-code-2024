def valid_report(report: list[int]) -> bool:
    for a, b in zip(report, report[1:]):
        if abs(a-b) < 1 or abs(a-b) > 3:
            return False
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False
    return True


with open("./day2/data.txt", "r") as f:
    safe = 0
    for line in f:
        line = list(map(int, line.split()))
        if valid_report(line):
            safe += 1
    print(f"{safe=}")
