"""In Bagels, a deductive logic game, you must guess the secret tree-digit number based on clues. 
    The game offers one of the following hints in response to your guess:
    'Pico' when your guess has the correct digit in the wrong place, 
    'Fermi' when your guess has the correct digit in the correct place, and
    'Bagels' if your guess has no correct digits.
    YOU HAVE 10 TRIES TO GUESS THE CORRECT NUMBER.
"""
import random

print("Bagels, a deductive logic game. By TYLONs17!")
cont = input("Would you like to continue? : Type YES or NO  \n")
res = cont[0].upper()

def bagels():
    count = 10
    if res == "N":
        print("Thanks for playing!")

    print("I AM THINKING OF A 3-DIGIT NUMBER. TRY TO GUESS WHAT IT IS.")
    print("Here are some clues:")
    print("When i say:            That means:")
    print("'Fermi'                 One digit is correct and in the right position.")
    print("'Pico'                  One digit is correct but in the wrong position.")
    print("'Bagels'                No digit is correct.")

    while count > 0 :
        
        print(f"I HAVE THOUGHT UP A NUMEBER. \n YOU HAVE {count} GUESSES TO GET IT.")
        
        guess = input("Enter a number: ")+"0"
        
        if guess[0] == "1"  and guess[1] == "7":
            print("You got it!")
            break
        elif guess[0] == "1" or guess[1] == "7":
            print("Fermi") 
        elif guess[0] == "7" and guess[1] == "1":
            print("Pico Pico")
        elif guess[0] == "7" or guess[1] == "1":
            print("Pico")
        else:
            print("Bagels")

        count -= 1
        
if res == "Y" or res == "N":
    bagels()
else:
    print("Please enter an appropriate response: (YES or NO)")


cont1 = input("Would you like to continue to a harder virsion? : Type YES or NO  \n")
res1 = cont1[0].upper()

def bagels1():
    count = 10
    if res == "N":
        print("Thanks for playing!")

    num_digits = input("Enter number of digits to guess: (3-10) ")
    if len(num_digits) > 2:
        num_digits = 3


    print(f"I AM THINKING OF A {num_digits}-DIGIT NUMBER. TRY TO GUESS WHAT IT IS.")
    print("Here are some clues:")
    print("When i say:            That means:")
    print("'Fermi'                 One digit is correct and in the right position.")
    print("'Pico'                  One digit is correct but in the wrong position.")
    print("'Bagels'                No digit is correct.")

    while count > 0 :
        
        print(f"I HAVE THOUGHT UP A NUMEBER. \n YOU HAVE {count} GUESSES TO GET IT.")
        
        guess = input("Enter a number: ")+"0"
        
        for char in num_digits:
            

            if guess[0] == "1"  and guess[1] == "7":
                print("You got it!")
                break
            elif guess[0] == "1" or guess[1] == "7":
                print("Fermi") 
            elif guess[0] == "7" and guess[1] == "1":
                print("Pico Pico")
            elif guess[0] == "7" or guess[1] == "1":
                print("Pico")
            else:
                print("Bagels")

        count -= 1
        
if res1 == "Y" or res1 == "N":
    bagels()
else:
    print("Please enter an appropriate response: (YES or NO)")
