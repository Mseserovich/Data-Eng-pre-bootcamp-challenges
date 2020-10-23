import math
def tri_area(a, b, c):
    """ Function that accepts 3 sides as input and returns
        area of triangle"""

    semi_p = 0.5 * (a + b + c)
    area = math.sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))
    return area

print(tri_area(3, 4, 5))