from math import *
from tabulate import tabulate


def main():
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

    equation = input("Enter f(x): ")
    x0 = float(input("Enter value of Xo+: "))
    x1 = float(input("Enter value of Xo-: "))
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

    print(tabulate(table, headers, tablefmt="pretty"))


if __name__ == "__main__":
    main()
