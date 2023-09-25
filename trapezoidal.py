from math import *
from tabulate import tabulate


def solve(equation, lowerLimit, upperLimit, should_print=False):
    b = eval(upperLimit)
    a = eval(lowerLimit)
    x = 0
    table = []
    for n in [2**i for i in range(12)]:
        h = (b - a) / n
        x = 0

        for i in range(n + 1):
            value = a + i * h
            if value == a or value == b:
                x += eval(equation.replace("x", str(value)))
            else:
                x += 2 * eval(equation.replace("x", str(value)))

        result = (h / 2) * x
        table.append([n, result])
    if should_print:
        print(tabulate(table, ["Panels", "Area"], tablefmt="simple"))
        return ""
    else:
        return table
