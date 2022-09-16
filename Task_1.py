number = 325
a, b, c, d, e = number + 25, number - 25, \
                number // 2, number % 25, number ** 0.5
print(a, b, c, d, e)

string = '325'
f, g, h, i, j = string + '0', string * 3, \
                string.join('a'), sorted(string), int(string) // 5
print(f, g, h, i, j)

l1st = [3, 2, 5]
l1st[1] = 0
l1st.sort()
print(l1st)

tupl3 = {}
for i in range(3):
    tupl3[i] = l1st[i]
print(tupl3)
