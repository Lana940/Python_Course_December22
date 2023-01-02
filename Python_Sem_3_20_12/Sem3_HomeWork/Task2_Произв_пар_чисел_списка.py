# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
from math import ceil  # Округляет в большую сторону  ceil(1)  # 1  ceil(1.1)  # 2 ceil(-1.1)  # -1 и тд
    
def mult_of_pairs(array):

    mult_list = []
    for i in range (ceil(len(array) / 2)):
        mult_list.append(array[i] * array[-(i + 1)])
    return mult_list

print(mult_of_pairs([2, 3, 4, 5, 6]))
print(mult_of_pairs([2, 3, 4, 5]))


exit()
# вариант из стрима:
my_list = [random.randint(1, 10) for i in range(10)]

new_list = []

for i in range(len(my_list) // 2):
    new_list.append(my_list[i]* my_list[-i - 1])

if len(my_list)%2 != 0: 
    new_list.append(my_list(len(my_list) // 2 )**2)      

print(my_list)    
print(new_list)
