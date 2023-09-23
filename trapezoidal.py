from math import *


def solve():
    print("""
Enter your equation
    Operations:
    + ADDITION
    - SUBTRACTION
    / DIVISION
    * MULTIPLY
    ** EXPONENT
    sqrt() SQUARE ROOT
    sin() SINE
    cos() COSINE
    tan() TANGENT
    e MATH CONSTANT EULER'S NUMBER\n\n""")
    equation = input("Enter equation: ")
    n = int(input("Enter number of strips: "))
    a = int(input("Enter lower limit: "))
    b = int(input("Enter upper limit: "))
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
    x = (h/2) * x
    print(f'{x:.5f}')


solve()
