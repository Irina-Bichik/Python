#Recursion and algorithms
# Task 20 (homework)
list_letters = {1: "AEIOULNSTRАВЕИНОРСТ",
                2: "DGДКЛМПУ",
                3: "BCMPБГЁЬЯ",
                4: "FHVWYЙЫ",
                5: "KЖЗХЦЧ",
                8: "JXШЭЮ",
                10: "QZФЩЪ"}

word = input("Введите слово: ").upper()  # НОУТБУК
summ = 0
for i in word:  # i = 'Н'
    for k, v in list_letters.items():
        if i in v:
            summ += k
print(f"Стоимость слова: {summ}")

# Task 24 (homework)
n = int(input())
array = [int(i) for i in input().split()][:n]
max_summa = 0
for i in range(1, len(array) - 1):
   if max_summa < array[i - 1] + array[i] + array[i + 1]:
      max_summa = array[i - 1] + array[i] + array[i + 1]

if max_summa < array[0] + array[1] + array[len(array) - 1]:
   max_summa = array[0] + array[1] + array[len(array) - 1]
if max_summa < array[0] + array[len(array) - 1] + array[len(array) - 2]:
   max_summa = array[0] + array[len(array) - 1] + array[len(array) - 2]
print(max_summa)

# Variant 2
n = int(input())
array = [int(input()) for i in range(n)]
sum_array = [array[i]+array[(i+1) % n]+array[(i+2) % n] for i in range(n)]
print(max(sum_array))


# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# Задание необходимо решать через рекурсию

def fib(n):
   if n in (0, 1):
      return n
   return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))
# 0 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5 6 7  8  9

# 0 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5 6 7  8  21
# fib(4) -> fib(3) + fib(2) = 2 + 1 = 3
#             |         |
#    fib(2) + fib(1)=1   fib(1)=1 + fib(0)=0
#      |
# fib(1) + fib(0) = 1 + 0 = 1
#   |        |
#   1        0

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

.sort()
sorted()
array = [5, 90, 34, 13, 54, 3, 12]
# array.sort()
array = sorted(array)
print(array)

n = int(input())
numbers = [int(i) for i in input().split()][:n]
new_numbers = [sorted(numbers)[0] if n == sorted(numbers)[-1] else n for n in numbers]
print(new_numbers)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# import math

def IsPrime(n):
   for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
         return 'no'

   return 'yes'

n = int(input())
print(IsPrime(n))

# 2^a * 3^b * 5^c
# 49 -> 1 7 49

# Variant 2
def IsPrime(num, div=2):  # рекурсия
    if num < div * div:
        return "yes"
    if num % div == 0:
        return "no"
    return IsPrime(num, div + 1)

n = int(input())
print(IsPrime(n))


# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3

def reverse_numbers(n):
   if n == 0:
      return ''
   k = int(input())
   return reverse_numbers(n - 1) + f' {k}'

n = int(input())
print(reverse_numbers(n))

# r(2) -> k = 3 -> r(1) + " 3" = " 4" + " 3" = " 4 3"
#                   |
#                  k = 4
#                   |
#                  r(0) + " 4" = "" + " 4" = " 4"
#                   |
#                   ""