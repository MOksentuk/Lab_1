n1=input()
symbs=['.', '-']
for i in range(10):
    symbs.append(str(i))

if any(x.isdigit for x in n1):
    print('y')
else:
    print('n')


def ch1(n1):
    if all([x in symbs for x in n1]):
        print('Введите второй элемент:')
        return float(n1)
    else:
        print('Введенный элемент не является числом,\
введите первый элемент:')
        n1 = input()
        return ch1(n1)
print(ch1(n1))


