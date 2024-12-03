f = open('input.txt')
# f = open('input_test.txt')


def save(report):
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


ss = 0
for line in f.readlines():
    if not line.strip():
        continue
    report = [int(x) for x in line.split()]
    s = save(report)
    print(line, s)
    ss += s

print(ss)
