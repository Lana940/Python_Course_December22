# Задайте список из n чисел последовательности (1 + 1/n)^n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


n = int(input("Введите число: "))
my_list = []
sum = 0

for i in range(1, n+1):

    num = (1 + 1 /i) **i
    num = round(num,2)
    my_list.append(num)

print(my_list)

for item in my_list:
    sum += item
print(sum)



