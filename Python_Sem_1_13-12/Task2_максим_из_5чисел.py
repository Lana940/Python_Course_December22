# напишите прогу, которая на вход принимает 5 чисел и находит максимальное из них 

my_list = []

for i in range(5):
     my_list.append(int(input("enter the number: ")))
print(my_list)

my_max = my_list[0]
for i in range(1, len(my_list)):
    if my_max < my_list[i]:
        my_max = my_list[i]

print(f"max number in my list is {my_max}")
