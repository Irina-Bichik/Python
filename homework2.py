# Циклы (for, while)

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input('Input the number of coins: '))
heads = 0
tails = 0
for i in range(n):
    count = int(input('Input - how the coin lies - up heads (1) or tails (2)? '))
    if count == 1:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(f'Minimum number of coins to be flipped is {tails} ')
if heads == tails:
    print(f'No need to flip the coins')
if heads < tails:
    print(f'Minimum number of coins to be flipped is {heads}')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

S = int(input('The sum of the numbers X and Y is \n'))
P = int(input('The product of the numbers X and Y is \n'))
for X in range(S):
    for Y in range(P):
        if S == X + Y and P == X * Y:
            print(f'The first number is "{X}", the second number is "{Y}"')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input('Input the number N: '))
# k=1
# while k<=N:
#     print(k,end=' ')
#     k=2*k


