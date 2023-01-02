# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи]

def fib(n):
    fib_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i %2 else x)
    return fib_list

fib_num = int(input("Enter number: "))
print(f' для k = {fib_num} -> {fib(fib_num)}')


exit()
# вариант со стрима:
fibo = [1,0,1]

for i in range(int(input("Введите предел последовательности: "))):
    fibo.insert(0, fibo[1] - fibo[0])
    fibo.append( fibo[-2] - fibo[-1])

print(fibo)