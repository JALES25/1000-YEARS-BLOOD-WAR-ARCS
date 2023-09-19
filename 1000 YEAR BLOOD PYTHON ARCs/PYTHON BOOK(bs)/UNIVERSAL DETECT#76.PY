
###scraped coz of the non imutable string
""""
board = \"""
#[-][-][-]                  [_1_][_2_][_3_]
#[-][-][-]                  [_4_][_5_][_6_]
#[-][-][-]                  [_7_][_8_][_9_]

\"""

bindex = []

for i in range(len(board)):
  if board[i] == "-":
      bindex.append(i)

newBoard = "change"

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

boardField = ["[-]","[-]","[-]","[-]","[-]","[-]","[-]","[-]","[-]"] 
boardID = ["[_1_]","[_2_]","[_3_]","[_4_]","[_5_]","[_6_]","[_7_]","[_8_]","[_9_]"]

spaces = "                                    "


def doBoard():
  outputBoard = ""
  for i in range(0,9,3):
   outputBoard += boardField[i]+boardField[i+1]+boardField[i+2] + spaces + boardID[i]+boardID[i+1]+boardID[i+2]+"\n"
   print(i)
   print(i+1)
   print(i+2)
  


doBoard()




