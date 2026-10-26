number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if choice == "1":
    result = add(number1, number2)
    print(f"Result: {result}")

elif choice == "2":
    result = subtract(number1, number2)
    print(f"Result: {result}")

elif choice == "3":
    result = multiply(number1, number2)
    print(f"Result: {result}")
    
elif choice == "4":
    try:
        result = divide(number1, number2)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
else:
    print("Invalid choice.")
