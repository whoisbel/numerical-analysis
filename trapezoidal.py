from math import *


def solve(equation, strips, lowerLimit, upperLimit):

    n = strips
    a = eval(lowerLimit)
    b = eval(upperLimit)
    h = (b-a)/n
    x = 0
    for i in range(int((b - a) / h) + 1):
        equation_display = ''
        value = a + i * h
        if (value == a or value == b):
            x += eval(equation.replace("x", str(value)))
            equation_display = f'{equation.replace("x", str(value))} = {eval(equation.replace("x", str(value))):.5f}'
            print(equation_display)
        else:
            x += 2 * eval(equation.replace("x", str(value)))
            equation_display = f'2 * ({equation.replace("x", str(value))}) = {2 * eval(equation.replace("x", str(value))):.5f}'
            print(equation_display)

    return (h/2) * x
