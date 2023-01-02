# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# not (x or y or z) == (not x and not y and not z):

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x or y or z) == (not x and not y and not z):
                print(f'Выражение при x ={x}, y={y}, z={z} верно')

# x y z 

# t t t
# t t f
# t f t
# t f f 

# f t t 
# f t f 
# f f t 
# f f t


