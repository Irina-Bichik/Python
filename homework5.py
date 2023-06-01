# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

a = int(input('Input number A: '))
b = int(input('Input number B: '))

def pov(a, b):
    if (b == 1):
        return a
    else:
        return a * pow(a, b - 1)
print(f'The number A to the integer power of B is {pov(a, b)}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

a = int(input('Input the first non-negative number '))
b = int(input("Input the second non-negative number "))

def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)

print(f'The sum of the numbers {a} and {b} is equal to {recursive_sum(a, b)}')