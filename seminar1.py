# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input("Введите число: "))
# i = 2
# result = 1
# while i <= n:
#     result *= i # result = result * i
#     i += 1
# print(f'{n}! = {result}')

# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# n = int(input("Введите число: "))
# a0 = 0
# a1 = 1
# a2 = 0
# i = 2
# while a2 < n:
#     a2 = a1 + a0 # Для того чтобы найти 3-ое число, мы складываем 1-ое и 2-ое
#     a0 = a1 # Для того чтобы найти 4-ое число, мы складываем 2-ое и 3-е
#     a1 = a2
#     i += 1
#     if a2 > n:
#         i = -1
# if i == -1:
#     print(i)
# else:
#     print(i)



# # for (int i = 0; i <= 10; i++)

# for i in 1, True, "Hello", 4.57:
#     print(i)

# # range()
# print(list(range(5)))
# for i in [0, 1, 2, 3, 4]:
#     print(i)

# begin = 10
# end = 0
# step = -1
# print(list(range(begin, end, step)))
# print(list(range(5))) # begin = 0           step = +1
# print(list(range(10, 20)))

# сколько дней длилась самая длинная оттепель
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 

# n = int(input("Ввдеите кол-во дней: "))
# count = 0
# max_days_count = 0
# for i in range(n):
#     x = int(input("Введите температуру сегодня: "))
#     if x > 0:
#         count += 1
#     else:
#         count = 0
    
#     if max_days_count < count:
#         max_days_count = count
# print(max_days_count)


# # Variant 2
# n = int(input("Ввдеите кол-во дней: "))
# count = 0
# max_days_count = 0
# # -10 30 -40 50 10 -20
# for i in range(n):
#     x = int(input("Введите температуру сегодня: "))
#     if x > 0:
#         count += 1
#     else:
#         if max_days_count < count:
#             max_days_count = count
#         count = 0
# print(max_days_count)

# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Выбрать самый легкий и самый тяжелый арбуз

n = int(input("Введите кол-во арбузов: "))
# a = [43, 13, 0, -10, 35, 89]
# 1 <= m <= 1000
max_massa = 0
min_massa = 1001
for i in range(n):
    x = int(input("Введите массу арбуза: "))
    if x > max_massa:
        max_massa = x

    if x < min_massa:
        min_massa = x
print(min_massa, max_massa)


