from math import *
from tabulate import tabulate


def solve(eq, initial_x, numIterations):

    if(not eq or not initial_x or not numIterations):
        return "Include complete input"
    equation = eq
    x = float(initial_x)
    k = int(numIterations)
    table = []
    absolute_error_threshold = 0.0009
    error = float('inf')

    for i in range(k):
        result = eval(equation.replace("x", str(x)))
        prev_x = x
        x = result
        error = (result - prev_x) / result
        table.append([i, f'{prev_x:.5f}', f'{result:.5f}', f'{error:.5f}'])

    headers = ["Iteration", "Xo", "Xo+1", "Relative Error"]

    if error > absolute_error_threshold:
        print("Diverging")
    else:
        print(f"Converging")

    return (tabulate(table, headers, tablefmt="pretty"))
