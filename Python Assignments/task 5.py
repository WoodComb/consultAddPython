# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
def one():
    try:
        eval("x === 4")
    except SyntaxError:
        print("There was a syntax error!")
one()

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
def two():
    import sys

    while True:
        try:
            filename = sys.argv[1]
            with open(filename, 'r') as f:
                contents = f.read()
            print(contents)
            break
        except (IndexError, FileNotFoundError):
            print("Invalid filename, please try again.")
            continue
two()
# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
def three():
    num = input("Enter a number with four digits: ")

    try:
        if len(num) != 4:
            raise ValueError("The length is too short/long !!! Please provide only four digits")
        num = int(num)
        print("You entered:", num)
    except ValueError as e:
        print("Error:", e)
three()
# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.
from getpass import getpass

def four():
    login = {
        "satya": "12345",
        "rohit": "67890",
        "mitali": "54321"
    }
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    tries = 3
    while login[username] != password and username in login.keys() and tries > 0:
        tries -= 1
        password = getpass("Re-enter your password: ")
    # Ask the user to re-type the password
    if tries < 0:
        print("INCORRECT")
    else:
        print("CORRECT")
four()

# 5. Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling


# 6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.
def six():
    with open("doc.txt", "r") as file:
        content = file.read()
        lines = content.split("\n")
        print(lines)
        line_lengths = [len(line) for line in lines]
        print(line_lengths)
        for index, i in enumerate(line_lengths):
            if i % 2 == 0:
                print(lines[index])
six()
