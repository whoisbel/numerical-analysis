import trapezoidal
from tabulate import tabulate
from math import *


def solve(func, lowerLimit, upperLimit):

    trapzoid = trapezoidal.solve(func, lowerLimit, upperLimit)

    table = []

    for i in range(5):
        table.append([trapzoid[i][0], '%.5f' % trapzoid[i][1], '', '', ''])
    for row in range(len(table)):
        for col in range(2, 5):
            if (col < row + 2):
                moreAccurate = table[row][1]
                lessAccurate = table[row-1][1]
                value = '%.5f' % (eval(f'{moreAccurate}') + (
                    eval(f'{moreAccurate}') - eval(f'{lessAccurate}')) / (4 ** (row + 1) - 1))

                table[row][col] = value

    headers = ['Strips', 'ITR', 'n=1', 'n=2', 'n=3']
    print(tabulate(table, headers, tablefmt="simple"))
    return ""
