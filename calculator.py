# Simple calculator program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print(f"Result: {num1 + num2}")
elif choice == "2":
    print(f"Result: {num1 - num2}")
elif choice == "3":
    print(f"Result: {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice!")