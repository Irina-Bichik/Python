# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# n = int(input('Input the number of elements in the array: '))
# arr = [int (i) for i in input ('Input array elements: ').split()]
# if len(arr) == n:
#    x = int (input('Input the element (X) you want to count: '))
#    count = 0
#    for i in range (n):
#      if arr[i] == x:
#          count +=1
# else:
#     print('More than N elements of the array')

# print(f'Element {x} repeats in the array {count} times')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Input the number of elements in the array (natural number N): '))
arr = []
for i in range(n):
    arr.append(int(input(f'Input the {i+1} element of the array ')))
x = int(input('Set the X element '))

m = abs(x - arr[0])
num = arr[0]
for i in range(1, len(arr)):
    if m > abs(x - arr[i]):
        m = abs(arr[i] - x)
        num = arr[i]
print(f'The closest element to the number {x} is {num}')


# n = abs(int(input('Введите количество элементов массива А: ')))
# Ai = input("Введите целые числа: ").split()
# A= list(map(int, Ai))
# if len(A) != n or n == 0:
#     print('Введенные элементы не соответствуют заявленному количеству')
# else:
    
#     X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
#     min = abs(X - A[0])
#     index = 0
#     for i in range(1, n):
#         count = abs(X - A[i])
#         if count < min:
#             min = count
#             index = i
#     print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')