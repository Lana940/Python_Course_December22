# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 1 вариант
text = ['sdfasjhaksjdfh', 'asdjalsdkj', 's', 'dfksk', 'efhwiehf', '56655', 'gdfb']
search = 'df'

for i in range(len(text)):   #для указания индекса
     if search in text[i]:     #in 
        print(f'подстрока встречается в искомом списке на индексе {i}')

# 2 вариант

list1 = ['jdsfb', '1378nhd', '5wefj8','ejkfh56', 'sdkl67','55', 'jkhkj665555']
x = input('enter symbol: ')

print(x in list1)
    
# 3 вариант
list1 = ["2", "43", "5", "331", "91", "35", "79", "53"]
x = input("enter number: ")

for i in list1:
   if x == i:
      print(f" chislo {i} est v spiske")
      break
else:
   print(f"chisla {x} net w spiske")
