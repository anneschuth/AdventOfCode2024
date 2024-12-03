f = open('input.txt')
# f = open('input_test.txt')

txt = f.read()

s = 0
for i in range(len(txt)):
    if txt[i:].startswith("mul("):
        mul = txt[i + 4:i + 14].split(")", 1)[0]
        try:
            print(mul)
            a, b = mul.split(",", 1)
            if a.isnumeric() and b.isnumeric():
                s += int(a) * int(b)
        except:
            # print(mul)
            continue
print(s)
