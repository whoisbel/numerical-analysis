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


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print("{:6.2f}".format(elem), end=" ")
        print()


A = [[2, -7, 4, 9],
     [1, 9, -6, 1],
     [-3, 8, 5, 6]]

solution = solve(A)


print("Final solution:")
for i, x_i in enumerate(solution):
    print(f"x{i + 1} = {x_i:.2f}")
