# ВЫВОД ДАННЫХ
print (5)
print (5, 8, 6)

'''
n = None
print (n)
'''

m = 1.89
print (m)

"""
a = 4
print (a)
"""
# ctrl+k и ctrl+c  /// убрать ctrl+k и ctrl+u
a = 'abcd'
print (a)

n = 5
print(type(n))

n = 'abcd'
print(type(n))

n = 'ab\'cd'   
m = 'ab"cd'   
print(n)
print(m)

a = 5
b = 5.89 
s = 'hello'

print(a, b, s)
print(a,'-', b,'-', s)
print('{} - {} - {}'.format(a,b,s))
print(f'first - {a} second - {b} third - {s}')

# ВВОД ДАННЫХ
print ('Ведите первую строку: ')
a = input()

b = input('Ведите второе число: ')

# Сумма двух чисел
# Приведение типов
c = 5.89 
n = int (c)
print(c)
print(n)

c = 5.89 
print(c)
print(type(c))
c = int(c)
print(c)
print(type(c))

c = 5.89 
c = str(c)
print(c + "89")
print(type(c))

c = 1
print(c)
print(type(c))

c = bool(c)
print(c)
print(type(c))

print ('Ведите первое число: ' )
a = int (input())

b = int (input('Ведите второе число: '))

print (a, '+', b, '=', a + b)

# Округление чисел
a = 5.89956
b = 6.556551
print(round (a*b, 3))

# Сокращенное присваивание
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

a = 1 > 4
print(a) 

a = 1 < 4 and 5 > 2
print(a)

a = 1 == 2
print(a) 

a = 1 != 2
print(a) 

a = 'qwe'
b = 'qwe'
print(a == b)

a = 1 < 3 < 5 < 10
print (a) 

# Управляющие конструкции: if, if-else, elif (else if)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

# Управляющие конструкции: while и вариация while-else   
n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)


i = 0
while i < 5:
    # if i == 3:
    #    break   
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)


n = 423
summa = 0
while n > 0:
      x = n % 10 # 3 2 4
      summa += x
      n = n // 10
else:
    print('Пожалуй')
    print('хватит )')
print(summa)

# Метод флажка
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1

# Цикл for, range
for i in 1, -2, 3, 14, 5:
    print(i)

# Range
# ● Range выдает значения из диапазона с шагом 1.
# ● Если указано только одно число — от 0 до заданного числа.
# ● Если нужен другой шаг, третьим аргументов можно задать приращение.

r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)

for i in range(5):
    print(i)

for i in 'qwerty':
    print(i)

# вложенные циклы
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

# Команды для работы со строками:
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))                        # Определить количество символов в строке
print('ещё' in text)                    # Проверить наличие символа в строке (in)
print(text.lower())                     # Функция, которая делает все буквы строки маленькими
print(text.upper())                     # Функция, которая делает все буквы строки большими
print(text.replace('ещё','ЕЩЁ'))        # Заменить слово на другое 

# Срезы
# ● Мы представляем строку в виде массива символов. Значит мы можем обращаться к элементам по индексам.
# ● Отрицательное число в индексе — счёт с конца строки

text = 'съешь ещё этих мягких французских булок'
print(text[0])                                  # c
print(text[1])                                  # ъ
print(text[len(text)-1])                        # к
# или
print(text[-1])                                 # к
print(text[-5])                                 # б
print(text[:])                                  # съешь ещё этих мягких французских булок
print(text[:2])                                 # съ
print(text[len(text)-2:])                       # ок
print(text[2:9])                                # ешь ещё
print(text[6:-18])                              # ещё этих мягких
print(text[0:len(text):6])                      # сеикакл
# или
print(text[::6])                                # сеикакл
text = text[2:9] + text[-5] + text[:2] 