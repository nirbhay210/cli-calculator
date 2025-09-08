# Python CLI-calcalculator - add, subtract,multiply, divide.

def add(a,b):
    return (a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    if b==0:
        return "Error: Division by Zero"
    return(a/b)
def main():
    print("welcome to cli-calculator!")
    print("operation: +, -, *, / (q to quit)")


    while True:
        choice = input ("\nchoose operation (+, -, * /) or q to quit: ").strip()

        if choice.lower() == "q":
            print("Exiting calculator. Goodbye!")
            break
        if choice not in ["+", "-", "*", "/"]:
            print("Invalid choice. Try again.")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "+":
            result = add(a, b)
        elif choice == "-":
            result = sub(a, b)
        elif choice == "*":
            result = mul(a, b)
        elif choice == "/":
            result = div(a, b)

        print("Result:", result)


if __name__ == "__main__":
    main()


