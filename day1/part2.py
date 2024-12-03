from collections import Counter

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


count_right = Counter(right)

s = 0
for l in left:
    s += l * count_right[l]

print(s)
