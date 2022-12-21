# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int
import random

def mix_list(original_list):

    mixed_list = original_list[:]
    mixed_list_length = len(original_list)

    for i in range(mixed_list_length):
        index_rand = random.randint(0, mixed_list_length - 1)
        temp = mixed_list[i]
        mixed_list[i] = mixed_list[index_rand]
        mixed_list[index_rand] = temp
    
    return mixed_list


original_list = [random.randint(0, 50) for i in range(random.randint(10, 20))]  # generator spiska
print(f'Исходный список: \n{original_list}')

mixed_list = mix_list(original_list)

print(f'Перемешанный список: \n{mixed_list}')




# random_list[1], random_list[8], random_list[14] = random_list[14], random_list[1], random_list[8]  - просто поменять местами
# # print(random_list)


# reversed(random_list)
# for i in reversed(random_list): print(i, end=' ')  - перевернуть список

# random.shuffle(random_list)   - встроенная функция шафл списка
# print(random_list)
