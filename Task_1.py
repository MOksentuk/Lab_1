# 1
#
# number = 325
# a, b, c, d, e = number + 25, number - 25, \
#                 number // 2, number % 25, number ** 0.5
# print(a, b, c, d, e)
#
# string = '325'
# f, g, h, i, j = string + '0', string * 3, \
#                 string.join('a'), sorted(string), int(string) // 5
# print(f, g, h, i, j)
#
# l1st = [3, 2, 5]
# l1st[1] = 0
# l1st.sort()
# print(l1st)
#
# tupl3 = {}
# for i in range(3):
#     tupl3[i] = l1st[i]
# print(tupl3)


# 2
funcs=['Сложение', 'Вычитание',"Умножение","Деление","Возведение в степень",\
       "Логарифм", "Округление в большую сторону до N знака после запятой", \
       "Округление в меньшую сторону до N знака после запятой"]
a='Введите необходимую функцию: сложение, вычитание, умножение, деление, \
возведение в степень, логарифм,\nокругление в большую сторону до N знака после запятой, \
округление в меньшую сторону до N знака после запятой.'
print(a)
def s(a,b):
       if int(a)!=a:
              print('Введенный элемент не является числом, введите первый элемент:')
def calc(f,n1,n2):
       if f not in funcs:
              print('Такой функции не существует.', a)
       elif f==funcs[0]:

print(s(5,6))