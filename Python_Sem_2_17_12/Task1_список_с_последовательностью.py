# Сформировать список из N членов последовательности.Для N = 5: 1, -3, 9, -27, 81 и т.д.

# posled * (-3)


N = int(input("Введите число: "))
a = 1

for i in range(N):
    print(a, end=' ')
    a = a * -3


# random posledovatelnost

import random 

n = int(input(" Enter the num: "))
for i in range(n):
    print(random.randint(0,10), end=' ')