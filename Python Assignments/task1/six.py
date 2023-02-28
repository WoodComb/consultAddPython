
input1 = input("Enter a value: ")

try:
    val = int(input1)
    print("Input is an integer number")
except ValueError:
    try:
        val = float(input1)
        print("Input is a float number")
    except ValueError:
        print("Input is a string")