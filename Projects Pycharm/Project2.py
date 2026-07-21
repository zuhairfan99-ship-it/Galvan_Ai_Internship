# Text Based Calculator
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in ["+", "-", "*", "/"]:
            return op
        print("Invalid operation. Please enter +, -, *, or /.")
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
def main():
    print("--- Text-Based Calculator ---")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = get_operation()
        result = calculate(num1, num2, operation)
        print(f"Result: {result}\n")
        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()