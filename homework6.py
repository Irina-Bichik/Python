# Repeating lists

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Input the first element of the arithmetic progression '))
d = int(input('Input difference '))
n = int(input('Input number of elements ' ))
for i in range(n):
    print(a1 + i * d, end=' ')

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_number = int(input('Input min number '))
max_number = int(input('Input max number '))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=' ')        