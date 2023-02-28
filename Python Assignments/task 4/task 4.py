# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
def one():
    a = "1234abcd"
    print(a[-1:0:-1])
one()

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
def two(s):
    lower, upper = 0, 0
    for l in s:
        if l.isupper(): upper+=1
        if l.islower(): lower+=1
    print(f"No. of Uppercase characters : {upper} No. of Lower case Characters : {lower}")
two("This is a SAMPLE stroing.")

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def three(lst):
    return list(set(lst))
print(three([1,2,3,1,2,3,4]))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
def four(s):
    a = [l for l in s.split("-")]
    a.sort()
    return "-".join(a)
print(four("h-e-l-l-o"))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
def five():
    lines = []
    while True:
        line = input("Enter a line (or press 'Enter' to stop): ")
        if line:
            lines.append(line)
        else:
            break
    for line in lines:
        print(line.upper())
five()    

# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
def six(a, b):
    print(int(a) + int(b))
six('3', '7')

# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
def seven(s1, s2):
    lens1 = len(s1) 
    lens2 = len(s2)
    if lens1 > lens2:
        print(s1)
    else:
        print(s2) 
    if lens1 == lens2:
        print(s1, " ", s1)

seven("hello", "hell00")

# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
def eight():
    print(tuple(i*i for i in range(1, 21)))
eight()

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
def showNumbers(limit):
    for i in range(limit+1):
        if i % 2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")
showNumbers(10)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
def ten():
    even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))
    print(even_numbers)
ten()

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.
def eleven():
    even_numbers = list(filter(lambda x: x % 2 == 0, range(1,11)))
    answer = list(map(lambda n: n*n, even_numbers))
    print(answer)
eleven()

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions13. 
def twelve():
    try:
        result = 5/0
        print("impossible!")
    except ZeroDivisionError:
        print("ZeroDivisionError will occur")
twelve()

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
def thirteen():
    def concatenate(a, b):
        return str(a) + str(b)
    result = reduce(concatenate, [1, 2, 3, 4, 5, 6, 7])
    print(int(result))
thirteen()

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
def fourteen():
    def check_num(num):
        return num % 3 != 0 and num % 7 == 0
    result = list(filter(check_num, range(1, 101)))
    print(result)
fourteen()

# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
def fifteen():
    def square(num):
        return num * num
    nums = [1, 2, 3, 4, 5]
    result = list(map(square, nums))
    print(result)

fifteen()

# 16. What is the output of the following codes:
# (i) def foo():
#       try:
#           return 1
#       finally:
#           return 2
#       k = foo()
#       print(k)

"""
Output : 2 
"""

# (ii) def a():
#       try:
#           f(x, 4)
#       finally:
#           print('after f')
#           print('after f?')
#      a()

"""
Output :  after f
          after f?

"""
