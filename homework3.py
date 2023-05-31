# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Input the number of elements in the array: '))
arr = [int (i) for i in input ('Input array elements: ').split()]
if len(arr) == n:
   x = int (input('Input the element (X) you want to count: '))
   count = 0
   for i in range (n):
     if arr[i] == x:
         count +=1
else:
    print('More than N elements of the array')

print(f'Element {x} repeats in the array {count} times')