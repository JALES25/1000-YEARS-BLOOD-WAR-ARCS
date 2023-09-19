""" BlackJack, also known as 21, is a card game where players try to get as close to 21 points as possible
    without going over. This program uses images drawn with text characters, ASCII art. 
    ASCCI is a mapping of text characters to numeric codes that computers used before unicode replaced it. 
    The playing cards in this program are an example of ASCII art: """

import random, sys

print()
print("BlackJack by TYLONs","\n")

print("The classic card game also known as 21. (This version doesn't have splitting or insurance)")



h_hand = """ 
##################
     ____   ____  
    |?   | |J   | 
    |  ? | |  + | 
    |___?| |___J|

################## """
f_hand = """ 
##################
     ____   ____  
    |A   | |J   | 
    |  + | |  + | 
    |___A| |___J|

################## """
draw = """ 
######## 
 _____  
|A````| 
|``+``| 
|____A| 
########
# """

card_num = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
card_group = [chr(9830),chr(9827),chr(9824),chr(9829)]
""" # ^ chr(9830) -> FOR DIAMONS
    # * chr(9827) -> FOR CLUBS
    # $ chr(9824) -> FOR SPADES
    # @ chr(9829) -> FOR HEARDS """

def gen_hands():
    dgen1 = random.choice(card_num)
    while dgen1 == 10:
       dgen1 = random.choice(card_num) 
    dgen2 = random.choice(card_num)
    while dgen2 == 10:
       dgen2 = random.choice(card_num)
    #Loop over each line in the sample_card var:
    for line in f_hand.splitlines():
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
                #Print first Card_num:
                print(dgen1, end="")
            elif sampleA == "J":
                #Print second Card_num:
                print(dgen2, end="")
            elif sampleA == "#":
                print("#", end="")
            elif sampleA == "+":
                #Print card_group:
                print(random.choice(card_group), end="") 
                 
        print()

def gen_hand():
    dgen1 = random.choice(card_num)
    while dgen1 == 10:
       dgen1 = random.choice(card_num) 
    #Loop over each line in the sample_card var:
    for line in h_hand.splitlines():
        #Loop over each character in the line:
        for i, sampleA  in  enumerate(line):
            if sampleA == "#":
                #Print top & bottom borders:
                print("#", end="")
            elif sampleA == " ":
                #Print an empty space since there's a space in the sample_card:
                print(" ", end="")
            elif sampleA == "_":
                #Print top & bottom borders:
                print("_", end="")
            elif sampleA == "|":
                #Print side borders:
                print("|", end="")
            elif sampleA == "?":
                #Print first Card:
                print("?", end="")
            elif sampleA == "J":
                #Print second Card_num:
                print(dgen1, end="")
            elif sampleA == "+":
                #Print card_group:
                print(random.choice(card_group), end="")
        print()

def gen_draw():
    dgen1 = random.choice(card_num)
    while dgen1 == 10:
       dgen1 = random.choice(card_num) 
    #Loop over each line in the sample_card var:
    for line in draw.splitlines():
        #Loop over each character in the line:
        for i, sampleA  in  enumerate(line):
            if sampleA == "#":
                #Print top & bottom borders:
                print("#", end="")
            elif sampleA == " ":
                #Print an empty space since there's a space in the sample_card:
                print(" ", end="")
            elif sampleA == "_":
                #Print top & bottom borders:
                print("_", end="")
            elif sampleA == "|":
                #Print side borders:
                print("|", end="")
            elif sampleA == "`":
                #Print `:
                print("`", end="")
            elif sampleA == "A":
                #Print Card_num:
                print(dgen1, end="")
            elif sampleA == "+":
                #Print card_group:
                print(random.choice(card_group), end="")
        print()

#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________

rules = """ Rules:
        Try to get as close to 21 without goiong over.
        Kings(K), Queens(Q) and Jacks(J) are worth 10 points. Aces(A) are worth 1 or 11 pints.
        cards 2 through 10 are worth their face value.
        Enter hit(H) to take another card. Enter stand(S) to stop taking cards.
        On your first play, you can double(D) down to increase your bet 
        but you must hit(H) exactly one more time before standing(S).
        In case of a tie the bet is returned to the player. The dealer stops hitting at 17
         """

#print(rules)

money = 5000

bet_1 = 100
bet_2 = 500
bet_3 = (1/2) * money
all_in = money

balance = "You have R" + str(money)
bet_range =   """How much do you want to bet?
    Bet ranges:
        Enter (1) for 100
        Enter (2) for 500
        Enter (3) for half your money
        Enter (4) for all in"""
#print(balance)
#print(bet_range)
#binp = input("> ")

#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________

######METHODS######
def getBet(maxBet):
    """ Ask the player how much they want to bet for this round. """
    while True: #Keep asking until they enter a valid amount.
        print("How much do you bet? (1 - {}, or QUIT(Q))".format(maxBet))
        bet = input("> ").upper().strip()

        if bet[0].upper() == "Q":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue #If the player didn't enter a number, ask again.

        bet = int(bet)  
        if 1 <= bet <= maxBet:
            return bet #Player entered a valid bet.

def getDeck(): 
    """Return a list of (rank, suit) tuple for all 52 cards."""
    deck = []
    for suit in (HEARDS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit)) #Add the numbered cards
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit)) #Add the face and ace cards
    #random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """ Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False. """
    print()
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        #Hide the dealers first card:
        displayCards([BACKSIDE] + dealerHand[1 : ])
        
    #Show the players cards:
    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)

def  getHandValue(cards):
    """ Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value) """
    value = 0
    numberOfAces = 0
    #Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] #card is a tuple like (rank, suit)
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K","Q","J"): #Face cards worth 10 points
            value += 10
        else:
            value +=  int(rank) #numbered cards worth their number.

    #Add the value for the aces:
    value += numberOfAces #Add 1 per ace.
    for i in range(numberOfAces):
        #If another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    """ Display all the cards in the card list. """
    rows = ["","","","",""] #Text to display on each fkn row.
    for i, card in enumerate(cards):
        rows[0] += "____" #Top part of card.
        if card == BACKSIDE:#Print cards back.             
            rows[1] += "|## |"
            rows[2] += "|###|" 
            rows[3] += "|_##|"
        else: #Print cars front.
            rank, suit = card #The card is a tuble data structure.
            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2,"_"))
            
    #Print each row on the screen:
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """ Asks the player for their move, and returns Hit(H), Stand(S), or Double down(D). """
    while True: #Keep looping until the player enters the correct move.
        #Dermine what move the player can make:
        moves = ["Hit(H)", "Stand(S)"]
        #The player can double down on their first move, which we tell because they'll have exatly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append("Double down(D)")
        #Get the player's move:
        movePrompt = ",".join(moves) + ">"
        move = input(movePrompt).upper()
        if move in ("H","S"):
            return move #Player has entered a valid move.
        if move == "D" and "Double down(D)" in moves:
            return move #Player has entered a valid move.
#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________

#Set up the constants
HEARDS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = "backside"

def main():
    print(rules)
    while True: #Ask until they give proper starting money:
        print("How much money do you need? R1_000 to R10_000 ")
        minp = input("> ")
        if minp.isdecimal():
            minp = int(minp)
            if 1_000 <= minp <= 10_000:
                break
    money = minp

    print(money)
    while True: #Main game loop.
        #check if the player has run out of money
        if money <= 0:
            print("You're a BROKEY")
            print("TF OUT OF MY SITE LITTLE PEASENT")
            sys.exit()
        
        #Let the player enter a bet for this round:
        print("Money:", money)
        bet = getBet(money)

        #Give the dealer and the player two cards from the deck each:
        deck = getDeck()

        dealerHand = [deck.pop(),deck.pop()]
        playerHand = [deck.pop(),deck.pop()]

        #Handle player actions:
        print("Bet:", bet)
        while True: #keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            #Check if player has bust:
            if  getHandValue(playerHand) > 21:
                break 

            #Get players move either Hit(H), Stand(S), or Double down(D):
            move = getMove(playerHand, money - bet)
        
            #Handle the player actions:
            if move == "D":
                #Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:",bet)

            if move in ("H","D"):
                #Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}.".format(rank,suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    #The player has busted:
                    continue

            if move in ("S", "D"):
                #Stand/doubling down stops the player turn.
                break

        #Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                #The dealer hits:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break #The dealer has busted.
                input("Press Enter to continue...")
                print("\n\n")

        #show the final hands:
        displayHands(playerHand, dealerHand, True)
        
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        #Handle whether the player won, lost or tied:
        if playerValue == [('A', '♠'), ('J', '♣')] or [('A', '♠'), ('J', '♣')]:
            money += bet * 10
        elif dealerValue > 21:
            print("Dealer Busts! Yus got lucky so You win R{}.".format(bet))
            money += bet
        elif (playerValue >= 21) or (playerValue < dealerValue):
            print("You're a loser! smh")
            print("if Yus keep loosing yul become a Brokey.")
            money -= bet
        elif playerValue > dealerValue:
            print("You popped off!, Yus a real G! so You win R{}".format(bet * 2))
            money += bet * 2 
        elif playerValue == dealerValue:
            print("""It's a tie, Yus becoming a Brokey so here's a handout...
                            The bet is returned to you.""")

        input("Press Enter to continue...")
        print("\n\n")


            

#If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()

                

        












#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________


