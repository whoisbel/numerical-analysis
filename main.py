import imports


def main():
    print("1. Root Finding")
    print("2. System of Linear Equations")
    print("3. Numerical Integration")
    user_input = input("Enter your choice (1/2/3): ")

    if user_input == "1":
        imports.utils.root_finding_menu()
    elif user_input == "2":
        imports.utils.linear_equations_menu()
    elif user_input == "3":
        imports.utils.numerical_integration_menu()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
