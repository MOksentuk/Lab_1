n1=input()
def ch1(n1):
    if n1.isdigit() or  type(n1) == float:
        print('Введите второй элемент:')
        return float(n1)
    else:
        print('Введенный элемент не является числом,\
введите первый элемент:')
        n1 = input()
        return ch1(n1)
# a=0.5383826
# if not type(a)==float:
#     print('no numb')
# else:
#     print(a)
# def ch1(n1):
#     if not n1.isdigit():
#         print('Введенный элемент не является числом,\
# введите первый элемент:')
#         n1 = input()
#         return ch1(n1)
#     else:
#         print('Введите второй элемент:')
#         return float(n1)
print(ch1(n1))