""" In this version of the two-player hand game also known as Jan-Ken-Pon, 
    the player faces of against the computer.
    You can pick either Rock, Paper or Scissors.
    Rock beats Scissors, Scissors beats Paper and Paper beats Rock.
    This program adds brief pauses for suspense.
 """
import random, time, sys

print("ROCK, PAPER, SCISSORS by TYLONs","\n")

rules = """ Here are the rules:
        - Rock beats Scissors.
        - Scissors bests Paper.
        - Paper beats Rock.

        ------NEW RULE--------
        - GUN beats everything
        ----------------------
         """

print(rules)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

class yikes():

    MOVES = ("ROCK","PAPER","SCISSORS")

    wins = 0
    losses = 0
    ties = 0

    doubles = 0
    points = 0

    def prompt():
        out = "You have {} Points from: {} Wins, {} Losses and {} Ties".format(yikes.points,yikes.wins,yikes.losses,yikes.ties)
        print(out)
        print()
        print("Enter your move: Rock(R)   Paper(P)   Scissors(S) or Quit(Q)")
        mov = input("> ")

        if mov == "":
            mov = " "

        player_move = mov [0].upper()

        #comp_move = random.choice(yikes.MOVES) #Generate computer move
        comp_move = yikes.MOVES[0]

        if player_move == "R": #If player picked ROCK
            player_move = yikes.MOVES[0]
            print(player_move,"versus...")
            yikes.do_pause()
            print(comp_move)
            yikes.do_result(player_move,comp_move) #Calculate the results

        elif player_move == "P": #If player picked PAPER
                player_move = yikes.MOVES[1]
                print(player_move,"versus...")
                yikes.do_pause()
                print(comp_move)
                yikes.do_result(player_move,comp_move) #Calculate the results
        
        elif player_move == "S": #If player picked SCISSORS
            player_move = yikes.MOVES[2]
            print(player_move,"versus...")
            yikes.do_pause()
            print(comp_move)
            yikes.do_result(player_move,comp_move) #Calculate the results


    def do_pause():
        for i in range(1,4):
            print("{}...".format(i)) 

    def do_result(move1,move2):

        if move1 == move2: #For tie
            print("IT'S A TIE!")
            yikes.ties += 1
            yikes.points += yikes.doubles
            yikes.doubles = 0

        elif (move1 == yikes.MOVES[0] and move2 == yikes.MOVES[1]) or (move1 == yikes.MOVES[1] and move2 == yikes.MOVES[2]) or (move1 == yikes.MOVES[2] and move2 == yikes.MOVES[0]): #The former loses
            print("YOU LOSE! ")
            print("You lossed a point!")
            yikes.losses += 1
            if yikes.doubles == 0:
                yikes.points -= 1
            else:
                yikes.points -= yikes.doubles
            yikes.doubles = 0
            
        elif (move1 == yikes.MOVES[1] and move2 == yikes.MOVES[0]) or (move1 == yikes.MOVES[2] and move2 == yikes.MOVES[1]) or (move1 == yikes.MOVES[0] and move2 == yikes.MOVES[2]): #The former wins
            print("YOU WIN!")
            yikes.wins += 1
            if yikes.doubles == 0:
                yikes.points += 1
            else:
                yikes.doubles += 1
                yikes.points += yikes.doubles * 2
            #Double or nothing 
            print("Go DOUBLE or NOTHING? Yes(Y) or press any key for no")
            ans = input("> ")
            if ans == "":
                ans = " "
            if ans[0].upper() ==  "Y":
                print("HERE WE GO...")
                yikes.prompt()
            else: 
                print("You gained a point!")
                yikes.points += 1
                yikes.doubles = 0
            
    def play():
        while True: #Main game loop
            out = "You have {} Points from: {} Wins, {} Losses and {} Ties".format(yikes.points,yikes.wins,yikes.losses,yikes.ties)
            print(out)
            print()
            print("Enter your move: Rock(R)   Paper(P)   Scissors(S) or Quit(Q)")
            mov = input("> ")

            if mov == "":
                mov = " "

            player_move = mov [0].upper()

            #comp_move = random.choice(yikes.MOVES) #Generate computer move
            comp_move = yikes.MOVES[0]

            if player_move == "Q": 
                print("GIVING UP ALREADY?" "\n")
                print("Ending session.....       Goodbye!")
                break #Loop out if they quit

            elif player_move == "R": #If player picked ROCK
                player_move = yikes.MOVES[0]
                print(player_move,"versus...")
                yikes.do_pause()
                print(comp_move)
                yikes.do_result(player_move,comp_move) #Calculate the results

            elif player_move == "P": #If player picked PAPER
                    player_move = yikes.MOVES[1]
                    print(player_move,"versus...")
                    yikes.do_pause()
                    print(comp_move)
                    yikes.do_result(player_move,comp_move) #Calculate the results
            
            elif player_move == "S": #If player picked SCISSORS
                player_move = yikes.MOVES[2]
                print(player_move,"versus...")
                yikes.do_pause()
                print(comp_move)
                yikes.do_result(player_move,comp_move) #Calculate the results

#yikes.play()           
#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

def playing():
    #These variables keep track of the number of wins, losses and ties.
    wins = 0
    losses = 0
    ties = 0

    while  True: #Main game loop.
        while True: #Keep asking until player enters R, P, S, or Q.
            print("{} Wins, {} Losses, {} Ties".format(wins,losses,ties))
            print("Enater your move: (R)ock (P)aper (S)cissors or (Q)uit")
            player_move = input("> ").upper()
            
            if player_move == "Q":
                print("Thanks for playing!")
                sys.exit()
            
            if player_move == "R" or player_move == "P" or player_move == "S":
                break
            else:
                print("Type one of R, P, S, or Q.")

        #Display what the player chose:
        if player_move == "R":
            print("ROCK versus...")
            player_move = "ROCK"
        elif player_move == "P":
            print("PAPER versus...")
            player_move = "PAPER"
        elif player_move == "S":
            print("SCISSORS versus...")
            player_move = "SCISSORS"
        
        #Count to three with dramatic pauses:
        time.sleep(0.5)
        print("1...")
        time.sleep(0.25)
        print("2...")
        time.sleep(0.25)
        print("3...")
        time.sleep(0.25)

        #Display what the computer chose:
        random_Number = random.randint(1,3)
        if random_Number == 1:
            computer_Move = "ROCK"
        elif random_Number == 2:
            computer_Move = "PAPER"
        elif random_Number == 3:
            computer_Move = "SCISSORS"
        print(computer_Move)
        time.sleep(0.5)

        #Display and record the win/loss/tie:
        if player_move == computer_Move:
            print("It's a tie!")
            ties += 1
        elif player_move == "ROCK" and computer_Move == "SCISSORS":
            print("You win!")
            wins += 1
        elif player_move == "PAPER" and computer_Move == "ROCK":
            print("You win!")
            wins += 1
        elif player_move == "SCISSORS" and computer_Move == "PAPER":
            print("You win!")
            wins += 1
        elif player_move == "ROCK" and computer_Move == "PAPER":
            print("You lose!")
            losses += 1
        elif player_move == "PAPER"  and computer_Move == "SCISSORS":
            print("You lose!")
            losses += 1
        elif player_move == "SCISSORS" and computer_Move == "ROCK":
            print("You lose!")
            losses += 1
             
 


        

  

    
    






  
