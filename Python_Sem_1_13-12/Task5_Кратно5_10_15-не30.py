#  Напишите программу, которая принимает на вход число и проверяет кратно ли оно 5 и 10 или 15, но не 30

num = int(input("Enter the number: "))

if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0)  and num % 30 != 0:
    print(f"Number {num} is multiple of 5, 10 or 15 and not multiple of 30 ")
else:
    print(f"The {num} is not multiple to provided numbers. Try another number." )