"""In Bagels, a deductive logic game, you must guess the secret tree-digit number based on clues. 
    The game offers one of the following hints in response to your guess:
    'Pico' when your guess has the correct digit in the wrong place, 
    'Fermi' when your guess has the correct digit in the correct place, and
    'Bagels' if your guess has no correct digits. 
    YOU HAVE 10 TRIES TO GUESS THE CORRECT NUMBER.
"""
import random

NUM_DIGITS = 3 # (!) Try setting this 1 or 10
MAX_GUESSES = 10 # (!) Try setting this to 1  or 100

def main():
    print("""Bagels, a deductive logic game. By TYLONs17! \n
    I AM THINKING OF A {}-DIGIT NUMBER. TRY TO GUESS WHAT IT IS.
    Here are some clues:
    When i say:            That means:
    'Fermi'                 One digit is correct and in the right position.
    'Pico'                  One digit is correct but in the wrong position.
    'Bagels'                No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843, the clues would be fermi pico.
    """.format(NUM_DIGITS))

    while True: # Main gamw loop
        # stores the secret number needs to guess
        secretNum = getSecretNum()
        print("I HAVE THOUGHT UP A NUMEBER. \n YOU HAVE {} GUESSES TO GET IT.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = " "
            #keeps looping until valid guess is entered :
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # Correct answer is found so breaks loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))
        #Ask player if they want to play again.
        print("Would you like to play again? (Yes or No)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")

def getSecretNum():
    #Return a string made up of NUM_DIGITS unique random digits.
    numbers = list("0123456789") # creates list of digits 0 - 9
    random.shuffle(numbers) #Shuffle into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = " "
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    #Returns a string with the pico, ferrmi, bagels clues for a guess and secret number pair.
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess[i] in  secretNum:
            #A a correct digit is in the corrct place.
            clues.append("Pico")
    if len(clues) == 0:
        #There are correct digits at all.
        return "Bagels"
    else:
        #Sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()
        #Make a single string from the list of  string clues.
        return " ".join(clues)

#If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main() 


#re-TRY TO MAKE A VERSION WITH LETTERS AS WELL AS DIGITS IN THE secretNum.

"""print("Bagels, a deductive logic game. By TYLONs17!")
cont = input("Would you like to continue? : Type YES or NO \n")
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
"""

