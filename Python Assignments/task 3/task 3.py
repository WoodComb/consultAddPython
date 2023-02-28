# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
def one():
    a = [1, 2, "three", "four", complex(5, 5), complex(6, 6), 7.1, 8.2, 9, 10.0]
    print(a)
one()
# 2. Create a list of size 5 and execute the slicing structure
def two():
    a = [1,2,3,4,5]
    print(a[2:4], a[-1::-1], a[4:2:-1])
two()
# 3. Write a program to get the sum and multiply of all the items in a given list.
def three():
    a = [1, 2, 3, 4, 5]
    print("sum ", sum(a))
    product = 1
    for i in a:
        product *= i
    print("product ", product)
three()

# 4. Find the largest and smallest number from a given list.
def four():
    a = [34, 65, 23, 7, 34, 285, 578, 42, 1, 0, 56, 3, -4, 6598]
    small = 0
    large = 0
    for i in a:
        small = min(small, i)
        large = max(large, i)
    print (f"smallest: {small}")
    print (f"largest: {large}")
four()

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.
def five():
    pred = [12,23,34,45,56,67,78,89,90]    
    res = [i for i in pred if i % 2 != 0]
    print(res)
five()

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).
def six():
    res = [i*i for i in range(1, 31) if i <= 5 or i >=26 ]
    print(res)
six()

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]
def seven():
    list1 = [1, 3, 5, 7, 9, 10]
    list2 = [2, 4, 6, 8]
    list1.pop()
    list1 += list2
    print(f"Combined list:-  {list1}No. of Uppercase characters : 3 No. of Lower case Characters : 12")
seven()
# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
def eight():
    a = {1 : 10, 2 : 20}
    b = {3 : 30, 4 : 40}
    for key in b.keys():
        a[key] = b[key]
    print(f"updated dict:  {a}")
eight()

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
def nine():
    n = 5
    res = {}
    for i in range(1, n+1):
        res[i] = i*i
    print(f"result:  {res}")
nine()
# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
def ten():
    nums = input("Enter numbers seperated just by a comma:  ")
    a = [int(n) for n in nums.split(",")]
    print(a, tuple(a))
ten()