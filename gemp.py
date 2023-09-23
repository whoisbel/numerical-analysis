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

        # Print the scaling step
        print(f"Step {i + 1}: Scale Row {i + 1} by {1 / pivot_element}")
        print("Before change matrix:")
        print_matrix(old_matrix)
        print("\nNew matrix:")
        print_matrix(A)
        input("Press Enter to continue...")

        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= factor * A[i][j]

            print(
                f"Step {i + 1}: Subtract {factor} times Row {i + 1} from Row {k + 1}")
            print("Before change matrix:")
            print_matrix(old_matrix)
            print("\nNew matrix:")
            print_matrix(A)
            input("Press Enter to continue...")

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][-1]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print("{:6.2f}".format(elem), end=" ")
        print()


# Define the augmented matrix A
A = [[2, -7, 4, 9],
     [1, 9, -6, 1],
     [-3, 8, 5, 6]]

solution = solve(A)

# Print the final solution
print("Final solution:")
for i, x_i in enumerate(solution):
    print(f"x{i + 1} = {x_i:.2f}")
