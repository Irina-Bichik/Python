data = [int(i) for i in input("Введите числа: ").split()]
print(data)

data = [int(i) for i in input("Введите числа: ").split()]
print(data)

list_1 = [1, -1.575, 'Hello, world!', True]
list
# array (import array || import numpy)
t = (1, 2)
t [0] += 1
# tuple 
# dict
# set
set_1 = {1, 2, 3, 4}
set_1.add(56)
print(*set_1)

# list() - set() - tuple()

# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

data = [int(i) for i in input("Введите числа: ").split()]
print(len(set(data)))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]

data = [int(i) for i in input("Введите числа: ").split()]
steps = int(input("Введите кол-во сдвигов: "))
steps = steps % len(data)
data = [data[i - steps] for i in range(len(data))]
print(data)

# i = 0: data[0 - 3]
# i = 1: data[1 - 3]
# i = 2: data[2 - 3]
# i = 3: data[3 - 3]
# i = 4: data[4 - 3]

# [10, 20, 30, 40, 50]
# -5  -4  -3  -2  -1
# steps = 3
# [30, 40, 50, 10, 20]
#  -3  -2  -1  -5  -4
#  0   1   2   3   4

data = [[1, -1.575], ['Hello, world', True], [15, -7]]
# # #           0                  1                 2
print(data[2][0])

data = {"Ivan": 27, 'Alexandr': 36, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'fotball']}}
# # key: value
print(data['Konstantin']['hobby'][0])



# data = [[1, -1.575], ['Hello, world', True], [15, -7]]
# #           0                  1                 2
# print(data[2][0])

# data = {"Ivan": 27, 'Alexandr': 36, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'fotball']}}
# # key: value
# print(data['Konstantin']['hobby'][0])
# # .values()
# # .keys()
# print(list(data.values()))
# print(list(data.keys()))




# data = [[1, -1.575], ['Hello, world', True], [15, -7]]
# #           0                  1                 2
# print(data[2][0])

# data = {"Ivan": 27, 'Alexandr': 36, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'fotball']}}
# # key: value
# print(data['Konstantin']['hobby'][0])
# # .values()
# # .keys()
# print(list(data.values()))
# print(list(data.keys()))
# print(list(data.items()))
# for k, v in data.items():
#     print(k, v)


# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"},
#            {"VIII":"S007"}]
# result = set()
# for item in data:
#     result.add(list(item.values())[0])
# print(result)

# вариант 2
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"},
#            {"VIII":"S007"}]
# result = set()
# for item in data:
#     for key in item:
#         result.add(item[key])
# print(result)


# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)

# data = [int(i) for i in input("Введите числа: ").split()]
# count = 0
# for i in range(len(data) - 1):
#     if data[i + 1] > data[i]:
#         count += 1
# print(count)




# data = [int(i) for i in input("Введите числа: ").split()]
# count = 0
# for i in range(len(data) - 1):
#     if data[i + 1] > data[i]:
#         count += 1
# print(count)
# n = 10
# print(int(n > 5))
# True - 1
# False - 0
# data = [int(i) for i in input("Введите числа: ").split()]
# print(sum([int(data[i + 1] > data[i]) for i in range(len(data) - 1)]))