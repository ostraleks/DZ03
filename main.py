# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
#
# out
# [4, 2, 4, 9]
# 8

# import random
# def rand(number):
#    list = []
#    for i in range (number):
#        list.append(random.randint(0, 100))
#    return list
# total_list = rand(int(input('Введите количество элементов списка ')))
# print(total_list, sum(total_list[::2]))


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
#
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

# import random, math
# def rand(number):
#     list = []
#     for i in range (number):
#         list.append(random.randint(0, 100))
#     return list

# def multiplication(num, input_list):
#     out_list =[]
#     for i in range (num // 2): 
#         out_list.append(input_list[i] * input_list[(num-1)-i])
#     if num % 2 > 0:
#         out_list.append(input_list[math.ceil(num // 2)])
#     return out_list  
# N = input('Введите количество элементов списка ')
# if N.isdigit() == False:
#     print ("Значение должно быть полжительным числом > 0")
# else:
#     total_list = rand(int(N))  
#     print(total_list, multiplication(int(N), total_list))


# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции
# преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011

# def to_binar(num):
#     temp = []
#     while num > 0:
#         temp.insert(0, num % 2)
#         num //= 2
#     print(*temp, sep='')
#     return temp

# to_binar(int(input('Введите число:'))) 


# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
#
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

# import random
# def rand(number):
#     list = []
#     for i in range (number):
#         list.append(random.random() * 100)
#         list[i] = round((list[i] - int(list[i])), 2)  
#     return list

# my_list = rand(int(input('Введите количество элементов: ')))
# print(my_list)
# print(f'\nmin number: {min(my_list)} \nmax number: {max(my_list)}')


# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fib(num):
    a, b = 1, 1
    num_fib = [0]
    for i in range(num):
        num_fib.append(a)
        num_fib.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return num_fib
print(fib(int(input('Задайте число: '))))
