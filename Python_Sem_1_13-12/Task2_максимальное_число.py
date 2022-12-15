# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

my_list = []

for i in range(5):  # цикл для ввода чисел, вместо 5 строк кода 
    my_list.append(int(input("enter number: ")))

print(my_list)
# print(max(my_list))  - встроенная функция

my_max = my_list[0]

for i in range(1, len(my_list)):    # уже не сравниваем 1 елемнт, ускоряем прогу ;)
    if my_max < my_list[i]:
        my_max = my_list[i]

print(f'max number in list is {my_max}')

# for item in my_list:  если сравнивать все елементы
#     if my_max < item:
#         my_max = item


# # for item in my_list:  - если брать сами елементы, а не индекс - елемнт изменить нельзя
#     print(item)
# for i in range (len(my_list)): #  а тут если по индексам, используя пробег по индексам, меняем значение елемнтов
       #  а тут если по индексам

# for i in range(1,10,2):  for i in range(a,b, c): gde a = ot, b = do, c = shag
#     print(i)
