# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def dec_to_bin(num: int):
    result = ''
    while num > 0:
        result = str(num %2) + result
        num //= 2
    return result


num = int(input("Enter dec num: "))
print(dec_to_bin(num))


exit()


# вариант со стрима:

number = int(input("enter int num: "))

bi_num = ''
while number > 0:
    bi_num = str(number %2) + bi_num
    number //= 2

print(bi_num) 