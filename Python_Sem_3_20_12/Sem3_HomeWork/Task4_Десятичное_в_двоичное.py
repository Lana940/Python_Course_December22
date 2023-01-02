# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input("enter int num: "))

bi_num = ''
while number > 0:
    bi_num = str(number %2) + bi_num
    number //= 2

print(bi_num) 