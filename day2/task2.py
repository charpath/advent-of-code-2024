def in_order(a: int, b: int, c: int) -> bool:
    return a > b > c or a < b < c


def valid_report(report: list[int]) -> bool:
    for a, b in zip(report, report[1:]):
        if abs(a-b) < 1 or abs(a-b) > 3:
            return False
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False
    return True


def valid_report_remove_one(report: list[int]) -> bool:
    if valid_report(report):
        return True
    for index in range(len(report)):
        if valid_report(report[:index] + report[index+1:]):
            return True
    return False


with open("./day2/data.txt", "r") as f:
    safe = 0
    for line in f:
        line = list(map(int, line.split()))
        if valid_report_remove_one(line):
            safe += 1
    print(f"{safe=}")
print(f"[1 2 3 2 1] is safe: {valid_report_remove_one([1, 2, 3, 2, 1])}")
