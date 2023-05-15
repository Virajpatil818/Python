print("Welcome to the Python Calculator!")
while True:
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
operation = input("Enter your choice: ")
if operation in ("1", "2", "3", "4", "5"):
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
if operation == "1":
print(first_number, "+", second_number, "=", first_number + second_number)
elif operation == "2":
print(first_number, "-", second_number, "=", first_number - second_number)
elif operation == "3":
print(first_number, "*", second_number, "=", first_number * second_number)
elif operation == "4":
print(first_number, "/", second_number, "=", first_number / second_number)
elif operation == "5":
print(first_number, "^", second_number, "=", first_number ** second_number)
continue_calculation = input("Continue calculation? (Y/N): ")
if continue_calculation == "N":
break
else:
print("Invalid input!")
