import copy

f = open('input.txt')
# f = open('input_test.txt')


def save_report(r):
    report = copy.deepcopy(r)
    x = report.pop(0)
    asc = None
    for y in report:
        if abs(x - y) > 3:
            return False
        a = 1 if y > x else -1 if y < x else 0
        if asc is not None and a != asc:
            return False
        elif asc is None:
            asc = a
        x = y
    return True


def save(report):
    if save_report(report):
        print(report)
        return True
    for i, _ in enumerate(report):
        r = copy.deepcopy(report)
        r.pop(i)
        if save_report(r):
            print(r)
            return True
    return False


ss = 0
for line in f.readlines():
    if not line.strip():
        continue
    report = [int(x) for x in line.split()]
    s = save(report)
    # print(line, s)
    ss += s

print(ss)
