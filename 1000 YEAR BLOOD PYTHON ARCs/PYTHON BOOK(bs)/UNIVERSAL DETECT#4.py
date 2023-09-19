import random


card_num = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
""" for i in range(1,14):
    card_num.append(i) """

card_group = ["^","*","$","@"]
# ^ -> FOR DIAMONS
# * -> FOR CLUBS
# $ -> FOR SPADES
# @ -> FOR HEARDS
sample_card = """
........ 
 _____  
|A````| 
|``+``| 
|____A| 
........
"""

new_card = []

def gen_card():
    #Loop over each line in the sample_card var:
    for line in sample_card.splitlines():
        #Loop over each character in the line:
        for i, sampleA  in  enumerate(line):
            if sampleA == " ":
                #Print an empty space since there's a space in the sample_card:
                print(" ", end="")
            elif sampleA == ".":
                #Print top & bottom borders:
                print(".", end="")
            elif sampleA == "`":
                print("`", end="")
            elif sampleA == "_":
                #Print top & bottom borders:
                print("_", end="")
            elif sampleA == "|":
                #Print side borders:
                print("|", end="")
            elif sampleA == "+":
                #Print card_group:
                print(random.choice(card_group), end="")
            elif sampleA == "A":
                #Print Card_num:
                print("A", end="")
        print()




""" #Print a character from the message:
    print(message[i % len(message)], end="") """

#____________________________________________________________________________________________________________

card = "hi"

def gen_card():
    dgen = random.choice(card_num)
    #Loop over each line in the sample_card var:
    for line in sample_card.splitlines():
        #Loop over each character in the line:
        for i, sampleA  in  enumerate(line):
            if sampleA == ".":
                #Print top & bottom borders:
                print(".", end="")
            elif sampleA == " ":
                #Print an empty space since there's a space in the sample_card:
                print(" ", end="")
            elif sampleA == "_":
                #Print top & bottom borders:
                print("_", end="")
            elif sampleA == "|":
                #Print side borders:
                print("|", end="")
            elif sampleA == "A":
                #Print Card_num:
                print(dgen, end="")
            elif sampleA == "`":
                print("`", end="")
            elif sampleA == "+":
                #Print card_group:
                print(random.choice(card_group), end="") 
                 
        print()


gen_card()