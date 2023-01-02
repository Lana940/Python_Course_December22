# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

my_list = [random.randint(1, 10) for i in range(10)]

new_list = []

for i in range(len(my_list) // 2):
    new_list.append(my_list[i]* my_list[-i - 1])

if len(my_list)%2 != 0: 
    new_list.append(my_list(len(my_list) // 2 )**2)      

print(my_list)    
print(new_list)
