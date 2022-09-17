
funcs = ['Сложение', 'Вычитание', "Умножение", "Деление", "Возведение в степень", \
         "Логарифм", "Округление в большую сторону до N знака после запятой", \
         "Округление в меньшую сторону до N знака после запятой"]

s = 'Введите необходимую функцию: 1.Сложение\n2.Вычитание\n3.Умножение\n4.Деление\n\
5.Возведение в степень\n6.Логарифм\n7.Округление в большую сторону до N знака после запятой\
\n8.Округление в меньшую сторону до N знака после запятой.'
print(s)
f, n1, n2 = input(), 0, 0

symbs=['.', '-']
for i in range(10):symbs.append(str(i))

def ch1(n1):
    if all([x in symbs for x in n1]):
        print('Введите второй элемент:')
        return float(n1)
    else:
        print('Введенный элемент не является числом,\
введите первый элемент:')
        n1 = input()
        return ch1(n1)


def ch2(n2):
    n2 = input()
    if all([x in symbs for x in n2]):
        return float(n2)
    else:
        print('Введенный элемент не является числом,\
    введите второй элемент:')
        n2 = input()
        return ch2(n2)


import math


def check(f, n1, n2):
    if str(f) not in funcs:
        print('Такой функции не существует.', s)
        f = input()
        return check(f, n1, n2)
    else:
        print('Введите первый элемент:')
        n1 = input()
        a, b = ch1(n1), ch2(n2)
        if f == funcs[0]:
            return a + b
        elif f == funcs[1]:
            return a - b
        elif f == funcs[2]:
            return a * b
        elif f == funcs[3]:
            return a / b
        elif f == funcs[4]:
            return a ** b
        elif f == funcs[5]:
            return math.log(a, b)
        elif f == funcs[6]:
            n = ''
            if b + 2 < len(str(a)):
                num = list(str(a)[:int(b) + 2])
                num[-1] = str(int(num[-1]) + 1)
                for i in range(len(num)): n += num[i]
                return n
            else:
                return a
        elif f == funcs[7]:
            return str(a)[:int(b)+2]


print(check(f, n1, n2))
