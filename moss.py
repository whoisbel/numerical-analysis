from math import *
from tabulate import tabulate


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

    equation = input("Enter equation: ")
    x = float(input("Enter initial value of x: "))
    k = int(input("Enter how many iterations: "))
    table = []
    absolute_error_threshold = 0.0000009
    error = float('inf')

    for i in range(k):
        result = eval(equation.replace("x", str(x)))
        prev_x = x
        x = result
        error = (result - prev_x) / result
        table.append([i, f'{prev_x:.5f}', f'{result:.5f}', f'{error:.5f}'])

    headers = ["Iteration", "Xo", "Xo+1", "Relative Error"]

    print(tabulate(table, headers, tablefmt="pretty"))

    if error > absolute_error_threshold:
        print("Diverging")
    else:
        print(f"Converging")
