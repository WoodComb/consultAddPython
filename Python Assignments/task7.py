# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.
import math

C, H = 50, 30
def calculate_Q(D):
    Q = math.sqrt((2 * C * D) / H)
    return Q

D = input("Enter the values of D (comma-separated): ")
D_list = [int(x) for x in D.split(',')]

for d in D_list:
    Q = calculate_Q(d)
    print("For D = {}, Q = {}".format(d, Q))



# 2. Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0: 
                    left += 1
                else: 
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res


# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours*60 + self.minutes
        print(f"{total_minutes} minute(s)")

    def addTime(self, t):
        minutes = self.minutes + t.minutes
        hours_in_minutes = (self.hours + t.hours) * 60
        total_minutes = minutes + hours_in_minutes
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Time(hours, minutes)
t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = t1.addTime(t2)
t3.displayTime() 
t3.displayMinute()

# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.
# Sample Input for amIOld():
# -1
# 4
# 10
# 16
# 18
# 64
# 38
# Expected Output for amIOld():
# Age is not valid, setting age to 0.
# You are young.
# You are young.
# You are a teenager.
# You are a teenager.
# You are old.
# You are old.
# Consider the age variable to be set to 38 then:
# Sample Input for yearPasses(): 4
# Expected Output for yearPasses(): 42
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def yearPasses(self, num):
        self.age += num

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age <= 19:
            print("You are a teenager.")
        else:
            print("You are old.")
