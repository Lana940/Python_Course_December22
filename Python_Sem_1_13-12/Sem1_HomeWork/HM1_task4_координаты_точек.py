# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant = int(input('quadrant = '))

if (0 < quadrant < 2):
    print(f'The possible range is X > 0, Y > 0')
if (1 < quadrant < 3):
    print(f'The possible range is X < 0, Y > 0')
if (2 < quadrant < 4):
    print(f'The possible range is X < 0, Y < 0')
if (3 < quadrant < 5):
    print(f'The possible range is X > 0, Y < 0')
elif quadrant >= 5:
    print(f'The "quadrant {quadrant}" does not exist')
