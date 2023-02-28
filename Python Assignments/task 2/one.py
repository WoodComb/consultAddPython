# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.

num = int(input("enter number "))
if num % 3 == 0:
    print("Consultadd", end = "")
if num % 5 == 0:
    if num % 3 == 0:
        print(" - ", end = "")
    print("Python Training")

print("")