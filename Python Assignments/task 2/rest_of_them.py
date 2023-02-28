# 8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6
# Digits 2
def eight():
    print("-----------------------------------------------------------------------------------------")

    string = input("Enter input: ")

    print(len(string))

    print("-----------------------------------------------------------------------------------------")

# 9. Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

def nine():
    print("-----------------------------------------------------------------------------------------")

    num = "25"
    choice = "yes"
    while choice != "no":
        ans = input("Guess the lucky number: ")
        if ans == num:
            choice = "no"
        else: 
            choice = input("Wanna try again? ")


    print("-----------------------------------------------------------------------------------------")

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”
def ten():
    print("-----------------------------------------------------------------------------------------")

    ans = "25"
    counter = 1
    while counter < 6:
        guess = input(f"Type in the number {counter}  ")
        counter += 1
        if guess == ans:
            print("good guess")
        else:
            print("try again")
    print("Game Over")

    print("-----------------------------------------------------------------------------------------")

# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.

def eleven():
    print("-----------------------------------------------------------------------------------------")

    ans = "25"
    counter = 1
    while counter < 6:
        guess = input(f"Type in the number {counter}  ")
        counter += 1
        if guess == ans:
            print("good guess")
            break
        else:
            print("try again")
    if counter == 6:
        print("Sorry but that wasnt so successful")
    else:
        print("Game over")

    print("-----------------------------------------------------------------------------------------")


eight()
nine()
ten()
eleven()