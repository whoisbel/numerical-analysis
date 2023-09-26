from math import *
from tabulate import tabulate


def solve(eq, x0, x1):

    if(not eq or not x0 or not x1):
        return "Include complete input"
    equation = eq
    table = []
    headers = ["Iteration", "Xo+",
               "Xo-", "Xo+1", "f(Xo+1)", "Relative Error"]
    result = 0
    i = 0
    while (True):
        x = 0.5*(x0 + x1)
        result = eval(equation.replace("x", str(x)))
        if result > 0:
            table.append([i, f'{x0:.4f}', f'{x1:.4f}',
                         f'{x:.4f}', f'{result:.4f}'])
            i += 1
            x0 = x
        else:
            table.append([i, f'{x0:.4f}', f'{x1:.4f}',
                         f'{x:.4f}', f'{result:.4f}'])
            i += 1
            x1 = x
        if (abs(result) < 0.001):
            table.append([i, f'{x0:.4f}', f'{x1:.4f}',
                         f'{x:.4f}', f'{result:.4f}'])
            break

    return tabulate(table, headers, tablefmt="pretty")
