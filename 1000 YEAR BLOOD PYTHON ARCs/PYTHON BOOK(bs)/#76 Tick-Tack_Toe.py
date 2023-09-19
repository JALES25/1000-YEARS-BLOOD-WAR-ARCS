"""Tick-Tack-Toe is a classic pencil & paper game played on a 3 x 3 grid.
   Players take turns placing their X or O marks, trying to get three in row.
   Most games of Tick-Tack-Toe end in a tie, but it is possible to outsmart your opponent if they're not careful.
   """


print("Welcome to Tick-Tack-Toe, by TYLONs", "\n")

#################################################
#strings arent immutable in python im switching to array as board
#board = """
#[-][-][-]                  [_1_][_2_][_3_]
#[-][-][-]                  [_4_][_5_][_6_]
#[-][-][-]                  [_7_][_8_][_9_]
#
#"""
"""moveX&O METHODS FOR THE DUM STRING SHIIII$#%$d%#%
def moveX(param):

   if param == 1:
      newBoard = board[:bindex[0]] + "X" + board[bindex[0]+1:]
      print(newBoard)
   elif param == 2:
      newBoard = board[:bindex[1]] + "X" + board[bindex[0]+1:]
   elif param == 3:
      newBoard = board[:bindex[2]] + "X" + board[bindex[0]+1:]
   elif param == 4:
      newBoard = board[:bindex[3]] + "X" + board[bindex[0]+1:]
   elif param == 5:
      newBoard = board[:bindex[4]] + "X" + board[bindex[0]+1:]
   elif param == 6:
      newBoard = board[:bindex[5]] + "X" + board[bindex[0]+1:]
   elif param == 7:
      newBoard = board[:bindex[6]] + "X" + board[bindex[0]+1:]
   elif param == 8:
      newBoard = board[:bindex[7]] + "X" + board[bindex[0]+1:]
   elif param == 9:
      newBoard = board[:bindex[8]] + "X" + board[bindex[0]+1:]

   print(newBoard)

def moveO(param):

   if param == 1:
      newBoard = board[:bindex[0]] + "O" + board[bindex[0]+1:]
      print(newBoard)
   elif param == 2:
      newBoard = board[:bindex[1]] + "O" + board[bindex[0]+1:]
   elif param == 3:
      newBoard = board[:bindex[2]] + "O" + board[bindex[0]+1:]
   elif param == 4:
      newBoard = board[:bindex[3]] + "O" + board[bindex[0]+1:]
   elif param == 5:
      newBoard = board[:bindex[4]] + "O" + board[bindex[0]+1:]
   elif param == 6:
      newBoard = board[:bindex[5]] + "O" + board[bindex[0]+1:]
   elif param == 7:
      newBoard = board[:bindex[6]] + "O" + board[bindex[0]+1:]
   elif param == 8:
      newBoard = board[:bindex[7]] + "O" + board[bindex[0]+1:]
   elif param == 9:
      newBoard = board[:bindex[8]] + "O" + board[bindex[0]+1:]

   print(newBoard)
"""
#I WILL TRY TO LEARN MORE ABOUT HOW TO MANIPULATE STRINGS
##################################################

#YAY NEW FIELD
boardField = ["[-]","[-]","[-]","[-]","[-]","[-]","[-]","[-]","[-]","[-]"] 
boardID = ["[_1_]","[_2_]","[_3_]","[_4_]","[_5_]","[_6_]","[_7_]","[_8_]","[_9_]"]

spaces = "                                    "

outputBoard = ""

# outputs the FIELD in a 3x3 format with their placeID places to the right also in a 3x3
def doBoard():
  outputBoard = ""
  for i in range(0,9,3):
   outputBoard += boardField[i]+boardField[i+1]+boardField[i+2] + spaces + boardID[i]+boardID[i+1]+boardID[i+2]+"\n"
  
  print("--snip--")
  print(outputBoard)
  print("--snip--")

#places X's move
def moveX(param):
   if param == 1:
      boardField[0] = "[X]"
   elif param == 2:
      boardField[1] = "[X]"
   elif param == 3:
      boardField[2] = "[X]"
   elif param == 4:
      boardField[3] = "[X]"
   elif param == 5:
      boardField[4] = "[X]"
   elif param == 6:
      boardField[5] = "[X]"
   elif param == 7:
      boardField[6] = "[X]"
   elif param == 8:
      boardField[7] = "[X]"
   elif param == 9:
      boardField[8] = "[X]"

#places O's move
def moveO(param):
   if param == 1:
      boardField[0] = "[O]"
   elif param == 2:
      boardField[1] = "[O]"
   elif param == 3:
      boardField[2] = "[O]"
   elif param == 4:
      boardField[3] = "[O]"
   elif param == 5:
      boardField[4] = "[O]"
   elif param == 6:
      boardField[5] = "[O]"
   elif param == 7:
      boardField[6] = "[O]"
   elif param == 8:
      boardField[7] = "[O]"
   elif param == 9:
      boardField[8] = "[O]"


#Prompting
def prompt():
   while True:
      doBoard()
      print()
      while True:
         x = int(input("What is X's move? Pick box number (1-9): "))
         if (boardField[x] != "[-]"):
            print("BOX ",x," IS TAKEN \n","Please select a box that is available")
         elif ((isinstance(x, int)) and boardField[x] == "[-]"):
            moveX(x)
            doBoard()
            if checkWin("X"):
               print("YAY")
               return  # Exit the function and the outer loop
            if "[-]" not in boardField:
                  print("It's a tie!")
                  return  # Exit the function and the outer loop
            break
      while True:
         o = int(input("What is O's move? Pick box number(1-9): "))
         if (boardField[o] != "[-]"):
            print("BOX ",x," IS TAKEN \n","Please select a box that is available")
         elif ((isinstance(o, int)) and boardField[o] == "[-]"):   
            moveO(o)
            doBoard()
            if checkWin("O"):
               print("YAY")
               return  # Exit the function and the outer loop
            if "[-]" not in boardField:
                  print("It's a tie!")
                  return  # Exit the function and the outer loop
            break
            break
      if ("[-]" not in boardField):
         break


""" ## DON MIND ME I'M JUST BEING USELESS
#############################
bindex = []  # Place holder for the index of the valid box move

for i in range(len(board)):
   if board[i] == "-":
      bindex.append(i) # Assigning the indexes of valid moves for use later

newBoard = ""  #Strings in python aren't immutable so this is a placeholder 

###### ME TOOO
def playermove(param):
"""



   
def checkWin(param):
   if ((boardField[0] == param and boardField[1] == param and boardField[2] == param) ):
      print("Congratulations", param, " ",param, "WINS UP-TOP HORIZONTALLY")
   elif ((boardField[3] == param and boardField[4] == param and boardField[5] == param) ):
      print("Congratulations", param, " ",param, "WINS IN THE CENTER HORIZONTALLY")
   elif ((boardField[6] == param and boardField[7] == param and boardField[8] == param) ):
      print("Congratulations", param, " ",param, "WINS IN THE DOWN-BOTTOM HORIZONTALLY")
   elif ((boardField[0] == param and boardField[3] == param and boardField[6] == param) ):
      print("Congratulations", param, " ",param, "WINS ON THE LEFT VERTICALLY")
   elif ((boardField[1] == param and boardField[4] == param and boardField[7] == param) ):
      print("Congratulations", param, " ",param, "WINS IN THE CENTER VERTICALLY")
   elif ((boardField[2] == param and boardField[5] == param and boardField[8] == param) ):
      print("Congratulations", param, " ",param, "WINS ON THE RIGHT VERTICALLY")
   elif ((boardField[0] == param and boardField[4] == param and boardField[8] == param) ):
      print("Congratulations", param, " ",param, "WINS FROM TOP-LEFT TO BOTTOM-RIGHT DIAGONALLY")
   elif ((boardField[6] == param and boardField[4] == param and boardField[2] == param) ):
      print("Congratulations", param, " ",param, "WINS FROM BOTTOM-LEFT TO TOP-RIGHT DIAGONALLY")
      

def whowon():
   print("Still calculating results. Please wait...")
    
#############################

print("--snip--")
prompt()
print("--snip--")
whowon()
print("Thanks for playing")