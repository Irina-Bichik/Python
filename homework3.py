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

# n = int(input('Input the number of elements in the array (natural number N): '))
# arr = []
# for i in range(n):
#     arr.append(int(input(f'Input the {i+1} element of the array ')))
# x = int(input('Set the X element '))

# m = abs(x - arr[0])
# num = arr[0]
# for i in range(1, len(arr)):
#     if m > abs(x - arr[i]):
#         m = abs(arr[i] - x)
#         num = arr[i]
# print(f'The closest element to the number {x} is {num}')

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко
# D, G – 2 очка 
# B, C, M, P – 3 очка
# F, H, V, W, Y – 4 очка 
# K – 5 очков
# J, X – 8 очков 
# Q, Z – 10 очков 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко 
# Д, К, Л, М, П, У – 2 очка 
# Б, Г, Ё, Ь, Я – 3 очка 
# Й, Ы – 4 очка 
# Ж, З, Х, Ц, Ч – 5 очков 
# Ш, Э, Ю – 8 очков 
# Ф, Щ, Ъ – 10 очков 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*
# ноутбук
#     12

eng_points = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
ru_points = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input('Input the world ').upper()
count = 0
for i in word:
    if i in 'abcdefghijklmnopqrstuvwxyz'.upper():    
        for j in eng_points:
            if i in eng_points[j]:
                count += j
    else:
        for j in ru_points:
            if i in ru_points[j]:
                count += j
print(f'The amount of points of the word {word} is {count}')
