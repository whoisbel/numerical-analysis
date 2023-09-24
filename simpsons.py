from math import *


def solve(equation, strips, lowerLimit, upperLimit):

    n = strips
    a = eval(lowerLimit)
    b = eval(upperLimit)
    h = (b-a)/n
    x = 0
    value = 0

    while (value <= b):
        equation_display = ''
        if (value == a or value == b):
            x += eval(equation.replace("x", str(value)))
            equation_display = f'{equation.replace("x", str(value))} = {eval(equation.replace("x", str(value)))}'
        else:
            x += 2 * eval(equation.replace("x", str(value)))
            equation_display = f'2 * {equation.replace("x", str(value))} = {eval(equation.replace("x", str(value)))}'
        value += h
        print(equation_display)

    return x * (b - a) / (2 * n)
