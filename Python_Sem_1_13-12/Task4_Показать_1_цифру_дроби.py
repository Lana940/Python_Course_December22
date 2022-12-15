# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = float(input(" enter number: "))
if int(num) - num == 0:
    print("Please enter float number")
else: 
    num = int(num*10%10)
    print(num)