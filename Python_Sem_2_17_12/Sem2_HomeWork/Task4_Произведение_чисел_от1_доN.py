# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try:
    n = int(input('enter num : '))
    mult = 1
    for i in range(1, n+1):
        mult*=i
        print(f'Mult of number from 1 to {n} : {mult}')
except:
    print('Put the NUMBER!')