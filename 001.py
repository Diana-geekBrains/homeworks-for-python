# Задача 2: Найдите сумму цифр трехзначного числа.

# a = int(input('Введите трехзначное число '))
# res = 0
# while a > 0:
#     res = res + a % 10
#     a = a//10
# print(res)

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок,если известно, что Петя и Сережа сделали 
#одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# S = int(input('Введите количество журавликов: '))
# x = S//6
# print(f'Петя и сережа сделали {x} журавликов каждый. Катя сделала {x*4} журавликов')

#  Вам требуется написать программу, которая проверяет счастливость билета.

# a  = input('Введите 6-ти значный номер билетика: ')
# sum1 = a[0] + a[1] + a[2]
# sum2 = a[3] + a[4] + a[5]
# if sum1 == sum2:
#     print('Он счастливый!')
# else:
#     print('Повезет в следующий раз!')


# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками

# n = int(input('Введите дольки по вертикали'))
# m = int(input('Введите дольки по горизотнали'))
# k = int(input('сколько долек хочешь отломить'))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('кушай свои дольки')
# else:
#     print('так не получится')

# семинар 2

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
#повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые 
#нужно перевернуть

# money = int(input('Введите кол-во монеток:'))
# tails = 0
# eagle = 0
# for _ in range (money):
#     value = int(input('Введите значения:'))
#     if value == 0:
#         tails += 1
#     else:
#         eagle += 1
# if tails > eagle:
#         print (eagle)
# else:
#     print (tails)

#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
#этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input('Введите сумму:'))
# p = int(input('Введите произведение:'))
# x = (s-((s**2-4*p)**0.5))//2
# y = (s+((s**2-4*p)**0.5))//2
# print(x, y)

#Задача 14: Требуется вывести все целые степени двойки (т.е. числа
#вида 2k), не превосходящие числа N.

# n = int(input( ))
# m = 1
# while m <= n:
#     print(m, end=' ')
#     m = m * 2

# семинар 3

# Требуется вычислить, сколько раз встречается некоторое число k в списке list_1.
# Найдите количество и выведите его.

# import random

# count = int(input('Введите кол-во элементов: '))
# some_list = []
# counter = 0
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

# k = int(input('Введите число К: '))
# counter = 0
# for i in some_list:
#     if i == k:
#         counter+=1
# print(counter)

# Требуется найти в массиве list_1 самый близкий по величине элемент
# к заданному числу k и вывести его.

# k = int(input('Введите число К: '))
# n = 0
# for i in range(len(some_list)):
#     if k == some_list[i]:
#         n = some_list[i]
#     elif k + 1 == some_list[i]:
#         n = some_list[i]
#     elif k-1 == some_list[i]:
#         n = some_list[i]
#     elif k+2 == some_list[i]:
#         n = some_list[i]
#     elif k-2 == some_list[i]:
#         n = some_list[i]
# print(n)  

# семинар 4

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input("Введите кол-во эл-ов 1-го множества "))
# list_1 = []
# list_2 = []

# for i in range (n):
#     list_1.append(int(input()))    

# m = int(input("Введите кол-во эл-ов 2-го множества "))
# for i in range (m):
#     list_2.append(int(input()))
# print (list_1, list_2)

# set_1 = set(list_1)
# set_2 = set(list_2)
# set_3 = set_1.intersection(set_2)
# print(sorted(set_3))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два 
# соседних. Всего на грядке растёт N кустов.Эти кусты обладают разной урожайностью, поэтому ко
# времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.В этом
# фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух 
# соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# import random
# num = int(input("Введите количество кустов "))
# a = []
# for _ in range (num):
#     b = random.randint(100, 1000)
#     a.append(b)
# print(a)
# max_sum = 0
# sum = 0
# for i in range (num-1):
#     sum = a[i-1] + a[i] + a[i+1]
#     if sum > max_sum:
#         max_sum = sum
# print(max_sum)

# семинар 5

# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.

# def f(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         return (a * f(a, b - 1))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a - 1, b + 1)
# print(sum(a, b))

# семинар 6

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a = int(input('Введите первый элемент '))
# b = int(input('введите шаг ')) 
# c = int(input('введите общее кол-во эл-тов ')) 

# for i in range(c):
#     print( a + i *b, end = " " )



# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# count = int(input('Введите кол-во элементов: '))
# some_list = []
# some_list_2 = []
# import random
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

# min_value = int(input('Введите минимальное знач-е: '))
# max_value = int(input('Введите максимальное знач-е: '))

# for ind in range(len(some_list)):
#     if some_list[ind] >= min_value and max_value >= some_list[ind]:
#         some_list_2.append(ind)  
# print(some_list_2)


































