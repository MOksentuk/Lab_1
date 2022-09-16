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
s='Введите необходимую функцию: Сложение, Вычитание, Умножение, деление, \
Возведение в степень, Логарифм,\nОкругление в большую сторону до N знака после запятой, \
Округление в меньшую сторону до N знака после запятой.'
print(s)
f, n1,n2=input(),0,0
def ch(f, n1, n2):
       if str(f) not in funcs:
              print('Такой функции не существует.', s)
              f=input()
              return ch(f, n1, n2)
       else:
              print('Введите первый элемент:')
              n1=input()
              if not n1.isdigit():
                     print('Введенный элемент не является числом,\
                      введите второй элемент:')
              else:
                     n1=int(n1)
                     print("Введите второй элемент:")
                     n2 = input()
                     if not n2.isdigit():
                            print('Введенный элемент не является числом,\
                              введите  первый элемент:')
                     else:
                            n2=int(n2)

# def calc(f,n1,n2):
#
#        elif f==funcs[0]:


print(ch(f,n1,n2))