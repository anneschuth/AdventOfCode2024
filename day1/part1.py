f = open('input.txt')
# f = open('input_test.txt')

left = []
right = []
for line in f.readlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))


s = 0
for l, r in zip(sorted(left), sorted(right)):
    s += abs(l-r)

print(s)
