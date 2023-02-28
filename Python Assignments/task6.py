# 1. Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.
def one(s = "Hello World"):
    uppercase_chars = [c for c in s if c.isupper()]
    print(uppercase_chars)
one()
# 2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
def two():
    students = ['Smit', 'Jaya', 'Rayyan']
    subjects = ['CSE', 'Networking', 'Operating System']
    result = {key: value for key, value in zip(students, subjects)}
    print(result)
two()
# 3. Learn More about Yield, next and Generators

# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
def three(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]

input_string = "Consultadd Training"
output_string = ''.join(three(input_string))
print(output_string)

# 5. Write an example on decorators.l

def wrapper(func):
    def inner():
        print("a wrapper")
        func()
    return inner

@wrapper
def normal():
    print("basic normal function")

normal()  