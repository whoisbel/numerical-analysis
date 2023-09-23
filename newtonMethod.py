from sympy import symbols, diff, lambdify
from tabulate import tabulate
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
        tan() TANGENT\n\n""")

    x = symbols('x')
    first_equation = input("Enter f(x): ")
    print(f"Derivative of {first_equation} is {diff(first_equation,x)}")
    second_equation = diff(first_equation, x)
    x0 = float(input("Enter initial value of x: "))
    k = int(input("Enter how many iterations: "))
    table = []
    headers = ["Iteration", "Xn", "f(Xn)", "f'(Xn)", "Xn+1", "Relative Error"]

    for i in range(k):
        f_xn = eval(first_equation.replace("x", str(x0)))
        f_prime_xn = eval(f'{second_equation}'.replace("x", str(x0)))
        x1 = x0 - (f_xn / f_prime_xn)
        error = abs((x1 - x0) / x1)
        table.append([i, f'{x0:.5f}', f'{f_xn:.5f}',
                     f'{f_prime_xn:.5f}', f'{x1:.5f}', f'{error:.5f}'])
        x0 = x1

    print(tabulate(table, headers, tablefmt="pretty"))
