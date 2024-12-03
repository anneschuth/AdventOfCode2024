f = open('input.txt')
# f = open('input_test.txt')

txt = f.read()

s = 0
enabled = True

for i in range(len(txt)):
    if txt[i:].startswith("don't()"):
        enabled = False
    elif txt[i:].startswith("do()"):
        enabled = True
    elif enabled and txt[i:].startswith("mul("):
        mul = txt[i + 4:i + 14].split(")", 1)[0]
        try:
            a, b = mul.split(",", 1)
            if a.isnumeric() and b.isnumeric():
                s += int(a) * int(b)
        except:
            continue

print(s)
