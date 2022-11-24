from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Radius must be real non-negative number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return pi * radius ** 2

# check_list = [1, 20, 37, -5, 2+3j, [1, 2,], True, 'string']

# for i in check_list:
#     print(f'Площадь окружности с радиусом {i} равна {circle_area(i)}')