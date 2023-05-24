# Ввод-Вывод, операторы ветвления

# Задача 2: Найдите сумму цифр трехзначного числа.
# # *Пример:*
# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0) |

n = int(input('Input a three-digit number: '))
n1 = n // 100
n2 = n // 10 % 10
n3 = n % 10
print(f'The sum of the digits of the number {n} is {n1 + n2 + n3} ({n1} + {n2} + {n3})')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

n = int(input('Input the number of cranes: '))
p = int (n/6)
k = int (2*n/3)
s = int (n/6)

print(p, k, s)
print (f'Petya made {p} cranes')
print (f'Katya made {k} cranes')
print (f'Sergey made {s} cranes')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input('Input the six-digit ticket number: '))
n1 = n//100000
n2 = n//10000 % 10
n3 = n//1000 % 10
n4 = n//100 % 10
n5 = n//10 %10
n6 = n % 10
sum1 = n1 + n2 + n3
sum2 = n4 +n5 +n6

f = sum1 == sum2
print (f)

# или 

if sum1 == sum2:
    print(f'Yes - the ticket number {n} is lucky')
else:
    print(f'No - the ticket number {n} is unlucky')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int (input ('Input number of slices (length n): '))
m = int (input ('Input number of slices (width m): '))
k = int(input('Input the number of slices you want to break off: '))

if k % n == 0 or k % m == 0:
    print(f'Yes - from a chocolate bar with a size of {n} x {m} slices, you can break off {k} slices')
else:
    print(f'No - it is impossible to break off {k} slices from a chocolate bar with a size of {n} x {m} slices')