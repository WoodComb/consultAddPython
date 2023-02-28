# 2. Write a program in Python to perform the following operator based task:
    # Ask user to choose the following option first:
    # If User Enter 1 - Addition
    # If User Enter 2 - Subtraction
    # If User Enter 3 - Division
    # If User Enter 4 - Multiplication
    # If User Enter 5 - Average
    # Ask user to enter two numbers and keep those numbers in variables num1 and num2
    # respectively for the first 4 options mentioned above.
    # Ask the user to enter two more numbers as first and second for calculating the average as
    # soon as the user chooses an option 5.
    # At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
    # note: At a time a user can only perform one action.


# Ask user to choose the operation
operation = int(input("Choose an operation:\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Average\n"))

# Ask user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the selected operation based on user's choice
if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = num1 / num2
elif operation == 4:
    result = num1 * num2
elif operation == 5:
    # Ask user to enter two more numbers
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = (num1 + num2 + first + second)/4

print(result)