file = open('text.txt', 'w', encoding = 'UTF-8')  # encoding = 'UTF-8'  - указать дла использования кирилицы
file.write('zapisat ety stroku')
file.close()


file = open('text.txt', 'r', encoding = 'UTF-8') 
data = file.readlines()
file.close()

print(data)

file = open('text.txt', 'r', encoding = 'UTF-8') 
data = file.read()
file.close()

print(data)
print(type(data))



file = open('text.txt', 'a', encoding = 'UTF-8') 
data = file.write('\neshe stroku dobawit')
file.close()

print(data)
print(type(data))


 with open('text.txt', 'a', encoding = 'UTF-8') as data:       #  если использовать конт менеджр with то файл закрывается автоматически
    data.write('dsagft')
    data.write('5454')

print(data)


from datetime import datetime

current_time = datetime.now()
print(current_time)