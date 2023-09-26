from tabulate import tabulate
from math import *


def solve(equation, lowerLimit, upperLimit, should_print=False):

    if not equation or not lowerLimit or not upperLimit:
        return "INCLUDE COMPLETE INPUT"
    b = eval(upperLimit)
    a = eval(lowerLimit)

    table_data = []

    for n in [2**i for i in range(12)]:
        h = (b - a) / n
        x = 0
        value = a

        while value <= b:
            if value == a or value == b:
                x += eval(equation.replace("x", str(value)))
            else:
                x += 2 * eval(equation.replace("x", str(value)))
            value += h

        result = x * (b - a) / (2 * n)
        table_data.append([n, result])

    if should_print:
        print(tabulate(table_data, ["Panels", "Area"], tablefmt="simple"))
        return ""
    else:
        return table_data
