# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# через строку:

n = input("введите вещ-e число: ")
sum = 0

for digit in n:
    if digit.isdigit():
        sum += int(digit)
print(f'Сумма цифр = {sum}')

# без строк

num = abs(float(input("Enter float number: ")))
# if num < 0:    - вместо этого модуль абс
#     num *= -1
while num % 1 != 0:
    num = round(num*10, 10)
print(num)

sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print(sum)