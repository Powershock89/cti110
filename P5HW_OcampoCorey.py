# Math Quiz
# 5-2-2023
# CTI-110 P5HW - Math Quiz
# Corey Ocampo
#

import random
def main():
   menu()


def menu():
   choice = 0
   while choice != 3:
    print("Welcome to the Math Quiz")
    print("")
    print("")
    print("Main Menu")
    print("-"*20)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print("")
    print("Please choose one of the menu options: ", end='')
    choice = int(input())


    if choice == 1:
        add()
        print("")
    elif choice == 2:
        subtract()
        print("")
    elif choice == 3:
        print("Thank you for playing...")
        print("Bye!!")
    else:
        print("Bad choice. Try again! ")
        print("")

def add():
    finished = 0
    guess = 0
    attempts = 0
    print("Addition Function")
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1 + num2
    print(f'  ',num1)
    print(f'+', num2)
    print("Enter answer. ")
    guess = int(input())

   

    while finished != 1:
        if guess < answer:
            attempts +=1
            print("Sorry, guess is too low.")
            print()
            print("Try again: ", end='')
            guess = int(input())
        elif guess > answer:
            attempts +=1
            print("Sorry, guess is too high.")
            print()
            print("Try again: ", end='')
            guess = int(input())
        else:
            attempts +=1
            print("Congratulations!!! Your guess is correct.")
            print(f'Number of guesses: {attempts}')
            print()
            finished = 1
    

def subtract():
    print("Subtraction Function")
    finished = 0
    guess = 0
    attempts = 0
    print("Addition Function")
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1 - num2
    print(f'  ',num1)
    print(f'- ', num2)
    print("Enter answer. ")
    guess = int(input())

   

    while finished != 1:
        if guess < answer:
            attempts +=1
            print("Sorry, guess is too low.")
            print()
            print("Try again: ", end='')
            guess = int(input())
        elif guess > answer:
            attempts +=1
            print("Sorry, guess is too high.")
            print()
            print("Try again: ", end='')
            guess = int(input())
        else:
            attempts +=1
            print("Congratulations!!! Your guess is correct.")
            print(f'Number of guesses: {attempts}')
            print()
            finished = 1



main()

