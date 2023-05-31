# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

stroka = input().split()
result = {}
for i in stroka:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1
print(result)

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore 
# The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore 
# I'm sure that the shells are sea shore shells

# Output: 13

input_str = "She sells sea shells   on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
a = input_str.upper() #
print(a)
b = a.split()
print(b)
c = set(b)
print(c)
d = len(c)
print (d)

print(len(set(input_str.upper().split())))

# Variant 2
text = input().split()
set_result = set()
for i in text:
    set_result.add(i.lower())
print(len(set_result))

# Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента 
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность).

n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
