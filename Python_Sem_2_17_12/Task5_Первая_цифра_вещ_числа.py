# Напишите прогу, которая на вход принимает дробь и покажет первую цифру дробной части числа: 
# Пример: 6,78 -> 7
#         5-> нет
#         0,34 -> 3

n = float(input("Put float number: "))

if (int(n) == n):
    print("Введите дробное число!")
else:
    print(int(abs(n) * 10)%10)