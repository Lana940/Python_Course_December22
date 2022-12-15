# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    X = int(input("Enter the X = "))
    Y = int(input("Enter the Y = "))

    A = None

    if (X > 0 and Y > 0):
        A = 1
        print(f'The point with coordinates {X}, {Y} lies in {A} quadrant')

    if (X < 0 and Y > 0):
        A = 2
        print(f'The point with coordinates {X}, {Y} lies in {A} quadrant')

    if (X < 0 and Y < 0):
        A = 3
        print(f'The point with coordinates {X}, {Y} lies in {A} quadrant')

    if (X > 0 and Y < 0):
        A = 4
        print(f'The point with coordinates {X}, {Y} lies in {A} quadrant')

except:
    print("Put the correct coordinates!")
