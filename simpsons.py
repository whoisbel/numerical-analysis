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
    a = eval(input("Enter lower limit: "))
    b = eval(input("Enter upper limit: "))
    h = (b-a)/n
    rule = int(input("1.) 1/3 Rule\n2.) 3/8 Rule\n>>> "))
    x = 0
    value = 0
    if (rule == 1):
        while (value <= b):
            if (value == a or value == b):
                x += eval(equation.replace("x", str(value)))
            else:
                x += 2 * eval(equation.replace("x", str(value)))
            value += h
        x *= (b - a) / (2 * n)
        print(x)
    elif (rule == 2):
        pass
    else:
        print("\nINVALID INPUT")


solve()
