# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("введите натуральное число: "))

my_dictionary = {} 
for i in range(1, n+1):
    my_dictionary[i] = 3*i + 1
print(my_dictionary)


n = int(input("введите натуральное число: "))

my_list =[]
for i in range(1, n+1):
    my_list.append([i, 3*i+1])
print(my_list)


n = int(input("введите натуральное число: "))
d ={a: 3*a +1 for a in range (1, n+1)}
print(d)