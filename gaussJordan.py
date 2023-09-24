
def input_matrix():
    matrix = []
    print("Enter each row of the matrix, separated by spaces:")

    while True:
        row_input = input("Enter a row (or press Enter to finish): ")

        if not row_input:
            break

        row = [float(x) for x in row_input.split()]
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print("{:6.2f}".format(elem), end=" ")
        print()


def solve(A):
    n = len(A)

    print("Initial matrix:")
    print_matrix(A)
    input("Press Enter to continue...")

    for i in range(n):
        pivot_row = A[i]
        pivot_element = pivot_row[i]

        old_matrix = [row[:] for row in A]

        for j in range(i, n + 1):
            pivot_row[j] /= pivot_element

        print(f"Step {i + 1}: Scale Row {i + 1} by {1 / pivot_element}")
        print("Before change matrix:")
        print_matrix(old_matrix)
        print("\nNew matrix:")
        print_matrix(A)
        input("Press Enter to continue...")

        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]
                print(
                    f"Step {i + 1}: Subtract {factor:.2f} times Row {i + 1} from Row {k + 1}")
                print("Before change matrix:")
                print_matrix(old_matrix)
                print("\nNew matrix:")
                print_matrix(A)
                input("Press Enter to continue...")

    solution = [row[-1] for row in A]

    return solution


def run():
    A = input_matrix()

    print("Matrix A:")
    print_matrix(A)

    solution = solve(A)

    print("\nFinal solution:")
    for i, x_i in enumerate(solution):
        print(f"x{i + 1} = {x_i:.2f}")
