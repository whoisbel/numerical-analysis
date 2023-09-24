from sympy import symbols, diff
from tabulate import tabulate
from math import *


def solve(eq, initial_x, numIteration):

    x = symbols('x')
    equation = eq
    print(f"Derivative of {equation} is {diff(equation,x)}")
    derivative = diff(equation, x)
    x0 = float(initial_x)
    k = int(numIteration)
    table = []
    headers = ["Iteration", "Xn", "f(Xn)", "f'(Xn)", "Xn+1", "Relative Error"]

    for i in range(k):
        f_xn = eval(equation.replace("x", str(x0)))
        f_prime_xn = eval(f'{derivative}'.replace("x", str(x0)))
        x1 = x0 - (f_xn / f_prime_xn)
        error = abs((x1 - x0) / x1)
        table.append([i, f'{x0:.5f}', f'{f_xn:.5f}',
                     f'{f_prime_xn:.5f}', f'{x1:.5f}', f'{error:.5f}'])
        x0 = x1

    return (tabulate(table, headers, tablefmt="pretty"))
