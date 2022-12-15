# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21     # AB = √(x2 - x1)2 + (y2 - y1)2

x1 = int(input(" x1 = "))
x2 = int(input(" x2 = "))
y1 = int(input(" y1 = "))
y2 = int(input(" y2 = "))

distance_between_points = None

distance_between_points = round(((x2 - x1) **2 + (y2 - y1) ** 2) ** 0.5, 2)

print(distance_between_points)