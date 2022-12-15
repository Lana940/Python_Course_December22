# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input("Enter day number: "))

my_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if num == (6 or 7):
    print(f'{my_list[num - 1]} is a weekend')
else:
    print(f'{my_list[num - 1]} is a working day')


