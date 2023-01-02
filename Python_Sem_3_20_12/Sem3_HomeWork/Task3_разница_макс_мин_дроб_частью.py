# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math 

from random import randint as RI  # можно заменять сокращением таким образом
from random import uniform as UF # uniform(x,y) -> возвращает случайнoе вещественное число r, такое, что х <= r и r < у


lenght_list = 5
# my_list = [round(RI(100,1000)/100, 2) for i in range(list_length)] если генерить рандомный лист
my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_tail_list = [round(my_list[i] - int(my_list[i]), 2) for i in range(lenght_list) if my_list[i] %1 != 0]


print(f'{my_tail_list} -> {max(my_tail_list) -  min(my_tail_list)}')


exit()

# вариант из стрима

my_list = [round(UF(0, 100), RI(0,3)) for _ in range(10)]

for _ in range(len(my_list)):
    item = my_list.pop(0)
    my_list.append(item if item != int(item) else int(item))               

print(my_list)

my_list = [x % 1 for x in my_list if x %1 != 0]

print(my_list)

