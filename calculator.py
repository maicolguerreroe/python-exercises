def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate():
    while True:
        print("Welcome to the calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        else:
            print("Invalid choice")

        while True:
            print("Do you want to continue? (Y/N)")
            choice = input()
            if choice == 'Y' or choice == 'y':
                calculate()
            elif choice == 'N' or choice == 'n':
                break
            else:
                print("Invalid choice")


def main():
    calculate()


if __name__ == '__main__':
    main()
