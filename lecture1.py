# ВЫВОД ДАННЫХ
# # print (5)
# print (5, 8, 6)
# '''
# n = None
# print (n)
# '''

# m = 1.89
# print (m)

# """
# a = 4
# print (a)
# """
# # ctrl+k и ctrl+c  /// убрать ctrl+k и ctrl+u
# # a = 'abcd'
# # print (a)

# n = 5
# print(type(n))

# n = 'abcd'
# print(type(n))

# n = 'ab\'cd'   
# m = 'ab"cd'   
# print(n)
# print(m)

# a = 5
# b = 5.89 
# s = 'hello'

# print(a, b, s)
# print(a,'-', b,'-', s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'first - {a} second - {b} third - {s}')

# ВВОД ДАННЫХ
# print ('Ведите первую строку: ')
# a = input()

# b = input('Ведите второе число: ')

# Сумма двух чисел
# Приведение типов
# c = 5.89 
# n = int (c)
# print(c)
# print(n)

# c = 5.89 
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# c = 5.89 
# c = str(c)
# print(c + "89")
# print(type(c))

# c = 1
# print(c)
# print(type(c))

# c = bool(c)
# print(c)
# print(type(c))

# print ('Ведите первое число: ' )
# a = int (input())

# b = int (input('Ведите второе число: '))

# print (a, '+', b, '=', a + b)

# Округление чисел
# a = 5.89956
# b = 6.556551
# print(round (a*b, 3))

# Сокращенное присваивание
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

# a = 1 > 4
# print(a) 

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a) 

# a = 1 != 2
# print(a) 

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5 < 10
# print (a) 

# Управляющие конструкции: if, if-else, elif (else if)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Управляющие конструкции: while и вариация while-else   
# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)


# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)


# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)


# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while


