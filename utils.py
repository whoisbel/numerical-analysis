# All DISPLAY/PRINTS/USER INPUT IN MAIN/ONLY UTILS HERE
import imports


def print_equation():
    """Print the list of available mathematical operations."""
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
    tan() TANGENT
    e MATH CONSTANT EULER'S NUMBER\n\n""")


def root_finding_menu():
    """Menu for Root Finding options."""
    print("1. Method of Successive Substitution")
    print("2. Newton's Method")
    print("3. Half-Interval Method (Bisection Method)")
    user_input = input("Enter your choice (1/2/3): ")

    if user_input == "1":
        print_equation()
        equation = input("Enter equation: ")
        x = input("Enter initial value of x: ")
        n = input("Enter number of iterations: ")
        print(imports.moss.solve(equation, x, n))
    elif user_input == "2":
        print_equation()
        equation = input("Enter equation: ")
        x = input("Enter initial value of x: ")
        n = input("Enter number of iterations: ")
        print(imports.newtonMethod.solve(equation, x, n))
    elif user_input == "3":
        print_equation()
        equation = input("Enter equation: ")
        x = float(input("Enter value of Xo+: "))
        n = float(input("Enter value of Xo-: "))
        print(imports.halfInterval.solve(equation, x, n))
    else:
        print("Invalid input. Please enter 1, 2, or 3.")


def linear_equations_menu():
    """Menu for System of Linear Equations options."""
    print("1. Gaussian Elimination with Maximum Pivot Strategy (GEMPS)")
    print("2. Gauss-Jordan method")
    user_input = input("Enter your choice (1/2): ")
    if user_input == "1":
        imports.gemp.run()
    elif user_input == "2":
        imports.gaussJordan.run()
    else:
        print("Invalid input. Please enter 1 or 2")


def numerical_integration_menu():
    """Menu for Numerical Integration options."""
    print("1. Trapezoidal Rule")
    print("2. Simpson's Rule")
    print("3. Romberg Integration")
    user_input = input("Enter your choice (1/2/3): ")
    if user_input == "1":
        print_equation()
        eq = input("Enter equation: ")
        n = int(input("Enter number of strips: "))
        l = input("Enter the value of lower limit: ")
        u = input("Enter the value of upper limit: ")
        print(imports.trapezoidal.solve(eq, n, l, u))
    elif user_input == "2":
        print_equation()
        eq = input("Enter equation: ")
        n = int(input("Enter number of strips: "))
        l = input("Enter the value of lower limit: ")
        u = input("Enter the value of upper limit: ")
        print(imports.simpsons.solve(eq, n, l, u))
    elif user_input == "3":
        print_equation()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
