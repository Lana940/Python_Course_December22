# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math 
from random import randint as RI 
from random import uniform as UF

my_list = [round(UF(0, 100), RI(0,3)) for _ in range(10) ]

for _ in range(len(my_list)):
    item = my_list.pop(0)
    my_list.append(item if item != int(item) else int(item))               

print(my_list)

my_list = [x % 1 for x in my_list if x %1 != 0]

print(my_list)

