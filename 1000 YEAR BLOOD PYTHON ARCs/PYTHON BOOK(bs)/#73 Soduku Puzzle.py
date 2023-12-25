""" Sudoku is a popular puzzle game in news-papers and mobile apps. 
    The Sudoku board is a 9 × 9 grid in which the player must place the digits 1 to 9 once, 
    and only once, in each row, column, and 3 × 3 subgrid. 
    The game begins with a few spaces already filled in with digits, called givens. 
    A well-formed Sudoku puzzle will have only one possible valid solution."""
 
import random
   
print("Welcome to Soduku Puzzle, by TYLONs17", "\n")

#################################################
#This will be the display pattern i will use
#board = """
#  A  B  C     E  F  G     H  I  J
#1[-][-][-] | [-][-][-] | [-][-][-]
#2[-][-][-] | [-][-][-] | [-][-][-]
#3[-][-][-] | [-][-][-] | [-][-][-]
# ---------- ----------- ----------
#4[-][-][-] | [-][-][-] | [-][-][-]
#5[-][-][-] | [-][-][-] | [-][-][-]
#6[-][-][-] | [-][-][-] | [-][-][-]
# ---------- ----------- ----------
#7[-][-][-] | [-][-][-] | [-][-][-]
#8[-][-][-] | [-][-][-] | [-][-][-]
#9[-][-][-] | [-][-][-] | [-][-][-]
#
#"""

#
lTop =   "    A    B    C         D    E    F         G    H    I"
subGrid1 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid2 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid3 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid4 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid5 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid6 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid7 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid8 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid9 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]

mainGrid = [[*subGrid1],[*subGrid2],[*subGrid3],[*subGrid4],[*subGrid5],[*subGrid6],[*subGrid7],[*subGrid8],[*subGrid9]]



vfillSpace = " | "
hfillSpace = "  ---------------     ---------------     ---------------"


#grid navigation
g0 = ['A1','A2','A3', 'B1','B2','B3', 'C1','C2','C3']
g1 = ['D1','E2','F3', 'D1','E2','F3', 'D1','E2','F3']
g2 = ['G1','H2','I3', 'G1','H2','I3', 'G1','H2','I3']

g3 = ['A4','A5','A6', 'B4','B5','B6', 'C4','C5','C6']
g4 = ['D4','E5','F6', 'D4','E5','F6', 'D4','E5','F6']
g5 = ['G4','H5','I6', 'G4','H5','I6', 'G4','H5','I6']

g6 = ['A7','A8','A9', 'B7','B8','B9', 'C7','C8','C9']
g7 = ['D7','E8','F9', 'D7','E8','F9', 'D7','E8','F9']
g8 = ['G7','H8','I9', 'G7','H8','I9', 'G7','H8','I9']

navGrid = [[*g0],[*g1],[*g2],[*g3],[*g4],[*g5],[*g6],[*g7],[*g8]]


# Board algos
class dogrid:
    # def __init__ (self, mainGrid, subG, rowG, colG):
    #     self.maingrid = mainGrid
    #     self.subG = subG
    #     self.rowG = rowG
    #     self.colG = colG
    
    
        # Algo to Display the Soduku Board
    def genBoard(): 
        outputBoard = "\n"
        
        outputBoard += lTop + "\n"
        rowNum = 0
        
        for i in range(0,9,3): # First subgrid row
            outputBoard += f"{rowNum+1} {mainGrid[0][i]}{mainGrid[0][i+1]}{mainGrid[0][i+2]} {vfillSpace} {mainGrid[1][i]}{mainGrid[1][i+1]}{mainGrid[1][i+2]} {vfillSpace} {mainGrid[2][i]}{mainGrid[2][i+1]}{mainGrid[2][i+2]} \n"
            rowNum += 1
            
        outputBoard += hfillSpace + "\n"
        
        for i in range(0,9,3): # Second subgrid row
            outputBoard += f"{rowNum+1} {mainGrid[3][i]}{mainGrid[3][i+1]}{mainGrid[3][i+2]} {vfillSpace} {mainGrid[4][i]}{mainGrid[4][i+1]}{mainGrid[4][i+2]} {vfillSpace} {mainGrid[5][i]}{mainGrid[5][i+1]}{mainGrid[5][i+2]} \n"
            rowNum += 1
        
        outputBoard += hfillSpace + "\n"
        
        # subGrid9[i+2] = [f'{9}'] # Don mind me im just existing for testing 
        for i in range(0,9,3): # Third subgrid row
            outputBoard += f"{rowNum+1} {mainGrid[6][i]}{mainGrid[6][i+1]}{mainGrid[6][i+2]} {vfillSpace} {mainGrid[7][i]}{mainGrid[7][i+1]}{mainGrid[7][i+2]} {vfillSpace} {mainGrid[8][i]}{mainGrid[8][i+1]}{mainGrid[8][i+2]} \n"
            rowNum += 1

        print("--snip--")
        print(outputBoard)
        print("--snip--")

       
    def checkPlacing(placing):
        subG = []
        rowG = []
        colG = []
        
        col = placing[0].upper()
        row = int(placing[1])
        
        def assignSubG(): 
            nonlocal subG
            if (col == 'A' and row <= 3) or (col == 'B' and row <= 3) or (col == 'C' and row <= 3):
                subG = mainGrid[0]
                return subG
            elif (col == 'A' and 4 <= row <= 6) or (col == 'B' and 4 <= row <= 6) or (col == 'C' and 4 <= row <= 6):
                subG = mainGrid[3]
                return subG
            elif (col == 'A' and 7 <= row <= 9) or (col == 'B' and 7 <= row <= 9) or (col == 'C' and 7 <= row <= 9):
                subG = mainGrid[6]
                return subG
            
            elif (col == 'D' and row <= 3) or (col == 'E' and row <= 3) or (col == 'F' and row <= 3):
                subG = mainGrid[1]
                return subG
            elif (col == 'D' and 4 <= row <= 6) or (col == 'E' and 4 <= row <= 6) or (col == 'F' and 4 <= row <= 6):
                subG = mainGrid[5]
                return subG
            elif (col == 'D' and 7 <= row <= 9) or (col == 'E' and 7 <= row <= 9) or (col == 'F' and 7 <= row <= 9):
                subG = mainGrid[7]
                return subG
                
            elif (col == 'H' and row <= 3) or (col == 'I' and row <= 3) or (col == 'J' and row <= 3):
                subG = mainGrid[2]
                return subG
            elif (col == 'H' and 4 <= row <= 6) or (col == 'I' and 4 <= row <= 6) or (col == 'J' and 4 <= row <= 6):
                subG = mainGrid[6]
                return subG
            elif (col == 'H' and 7 <= row <= 9) or (col == 'I' and 7 <= row <= 9) or (col == 'J' and 7 <= row <= 9):
                subG = mainGrid[8]
                return subG    
        assignSubG()
        
        def assignRow():
            if (row == 1):
                rowG.extend([mainGrid[0][0], mainGrid[0][1], mainGrid[0][2], mainGrid[1][0], mainGrid[1][1], mainGrid[1][2], mainGrid[2][0], mainGrid[2][1], mainGrid[2][2]])
            elif (row == 2):
                rowG.extend([mainGrid[0][3], mainGrid[0][4], mainGrid[0][5], mainGrid[1][3], mainGrid[1][4], mainGrid[1][5], mainGrid[2][3], mainGrid[2][4], mainGrid[2][5]])
            elif (row == 3):
                rowG.extend([mainGrid[0][6], mainGrid[0][7], mainGrid[0][8], mainGrid[1][6], mainGrid[1][7], mainGrid[1][8], mainGrid[2][6], mainGrid[2][7], mainGrid[2][8]])
                
            elif (row == 4):
                rowG.extend([mainGrid[3][0], mainGrid[3][1], mainGrid[3][2], mainGrid[4][0], mainGrid[4][1], mainGrid[4][2], mainGrid[5][0], mainGrid[5][1], mainGrid[5][2]])
            elif (row == 5):
                rowG.extend([mainGrid[3][3], mainGrid[3][4], mainGrid[3][5], mainGrid[4][3], mainGrid[4][4], mainGrid[4][5], mainGrid[5][3], mainGrid[5][4], mainGrid[5][5]])
            elif (row == 6):
                rowG.extend([mainGrid[3][6], mainGrid[3][7], mainGrid[3][8], mainGrid[4][6], mainGrid[4][7], mainGrid[4][8], mainGrid[5][6], mainGrid[5][7], mainGrid[5][8]])
                
            elif (row == 7):
                rowG.extend([mainGrid[6][0], mainGrid[6][1], mainGrid[6][2], mainGrid[7][0], mainGrid[7][1], mainGrid[7][2], mainGrid[8][0], mainGrid[8][1], mainGrid[8][2]])
            elif (row == 8):
                rowG.extend([mainGrid[6][3], mainGrid[6][4], mainGrid[6][5], mainGrid[7][3], mainGrid[7][4], mainGrid[7][5], mainGrid[8][3], mainGrid[8][4], mainGrid[8][5]])
            elif (row == 9):
                rowG.extend([mainGrid[6][6], mainGrid[6][7], mainGrid[6][8], mainGrid[7][6], mainGrid[7][7], mainGrid[7][8], mainGrid[8][6], mainGrid[8][7], mainGrid[8][8]])
        assignRow()
        
        def assignCol():
            if (col == 'A'):
                colG.extend([mainGrid[0][0], mainGrid[0][3], mainGrid[0][6], mainGrid[3][0], mainGrid[3][3], mainGrid[3][6], mainGrid[6][0], mainGrid[6][3], mainGrid[6][6]])
            elif (col == 'B'):
                colG.extend([mainGrid[0][1], mainGrid[0][4], mainGrid[0][7], mainGrid[3][1], mainGrid[3][4], mainGrid[3][7], mainGrid[6][1], mainGrid[6][4], mainGrid[6][7]])
            elif (col == 'C'):
                colG.extend([mainGrid[0][2], mainGrid[0][5], mainGrid[0][8], mainGrid[3][2], mainGrid[3][5], mainGrid[3][8], mainGrid[6][2], mainGrid[6][5], mainGrid[6][8]])
            
            elif (col == 'D'):
                colG.extend([mainGrid[1][0], mainGrid[1][3], mainGrid[1][6], mainGrid[4][0], mainGrid[4][3], mainGrid[4][6], mainGrid[7][0], mainGrid[7][3], mainGrid[7][6]])
            elif (col == 'E'):
                colG.extend([mainGrid[1][1], mainGrid[1][4], mainGrid[1][7], mainGrid[4][1], mainGrid[4][4], mainGrid[4][7], mainGrid[7][1], mainGrid[7][4], mainGrid[7][7]])
            elif (col == 'F'):
                colG.extend([mainGrid[1][2], mainGrid[1][5], mainGrid[1][8], mainGrid[4][2], mainGrid[4][5], mainGrid[4][8], mainGrid[7][2], mainGrid[7][5], mainGrid[7][8]])
            
            if (col == 'G'):
                colG.extend([mainGrid[2][0], mainGrid[2][3], mainGrid[2][6], mainGrid[5][0], mainGrid[5][3], mainGrid[5][6], mainGrid[8][0], mainGrid[8][3], mainGrid[8][6]])
            elif (col == 'H'):
                colG.extend([mainGrid[2][1], mainGrid[2][4], mainGrid[2][7], mainGrid[5][1], mainGrid[5][4], mainGrid[5][7], mainGrid[8][1], mainGrid[8][4], mainGrid[8][7]])
            elif (col == 'I'):
                colG.extend([mainGrid[2][2], mainGrid[2][5], mainGrid[2][8], mainGrid[5][2], mainGrid[5][5], mainGrid[5][8], mainGrid[8][2], mainGrid[8][5], mainGrid[8][8]])
        assignCol()

        placingObj = {
            "subG": subG,
            "rowG": rowG,
            "colG": colG
        }
        
        return placingObj
    # checkPlacing(placing)

    
    def validate(placing):
        placings = dogrid.checkPlacing(placing)
        subG = placings["subG"]
        rowG = placings["rowG"]
        colG = placings["colG"]

        # print(placing)
        # print('------')
        # print(subG)
        # print(rowG)
        # print(colG)
        # print('------')
        col = placing[0].upper()
        row = int(placing[1])
        num = int(placing[3]) if len(placing) == 4 else None
        
        if num == None:
            # print("Number to check not given or something went wrong \t Can't be bothered to check so it's whatever")
            return False
        
        def notInSubGrid(arr, num): 
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        return False
            return True  #Supposed to return true when num not in subGrid
        
        def notInColumn(arr, num):
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        return False
            return True  #Supposed to return true when num not in Column
            
        def notInRow(arr, num):
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        return False
            return True  #Supposed to return true when num not in Row
        
            
        if (notInSubGrid(subG, num) and notInRow(rowG, num) and notInColumn(colG, num)):
            # print("Number does not exist in grid or something went wrong but is passes still, \t Can't be bothered to check so it's whatever")
            return True
        else:
            # print("Number already exists in grid")
            return False
            
    
    def genNumbs():
        
        # def checkEmpty(arr):
        #     noEmpty = True
        #     for i in range(len(arr)):
        #         if not(isinstance(int(arr[i][0]), (int, float))):
        #             noEmpty = False
        #     return noEmpty
        
        def checkEmpty(main_grid):
            """
            Check if the main grid contains any cell with the value ["-"]. Which represents th default empty value
            """
            for subgrid in main_grid:
                if any(cell == ["-"] for row in subgrid for cell in row):
                    return True  # If any cell with value ["-"] is found, return True
                
                

            return False  # If no such cell is found, return False

        
        # i want to iterate through the mainGrid and the navGrid so that the dogrid.validate() gets the co-ordinates of cell 
        def gengrid(arr1, arr2):
            while True:
                for index, (arr1, arr2) in enumerate(zip(arr1, arr2)):
                    # print(arr1)
                    # print(arr2)
                    
                    for place, key in zip(arr1, arr2):
                        num = random.randint(1,9)
                        placing = f'{key} {num}'
                        
                        # print(place[0], placing)

                        if dogrid.validate(placing):
                            place[0] = placing[3]
                       
                    # placing = f'{arr2[index]} {num}'
                    # if (dogrid.validate(placing)): # nothing like a 40 min rant/tantrun to then say no theres a better way 
                    #     arr1[index][0] = f'{num}'
                        
                # dogrid.genBoard()
                    
                if checkEmpty(arr1) == False:
                    break
         

        for i in range(len(mainGrid)):
            # gensubgrid(mainGrid[i])
            gengrid(mainGrid, navGrid)
            
    
    
 
    


FirstBoard =  dogrid.genNumbs()  # dogrid.genNums() method currently has no return implementation -- yes yes i knw
dogrid.genBoard()





# print("Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:", "For example, a move looks like 'B4 9'")
# print("--snip--")









class Utils: 
    def validate(move):
        placings = dogrid.checkPlacing(move)
        subG = placings["subG"]
        print(subG)
        rowG = placings["rowG"]
        print(rowG)
        colG = placings["colG"]
        print(colG)
        
        # col = move[0].upper()
        # row = int(move[1])
        num = int(move[3]) if len(move) == 4 else None
        
        if num == None:
            # print("Number to check not given or something went wrong \t Can't be bothered to check so it's whatever")
            return False
        
        def notInSubGrid(arr, num): 
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        print("check - subgrid already has that number")
                        return False
            return True  #Supposed to return true when num not in subGrid
        
        def notInRow(arr, num):
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        print("check2 - \t already in the row")
                        return False
            return True  #Supposed to return true when num not in Row
        
        def notInColumn(arr, num):
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        print("check3B - \t number exists in the column")
                        return False
            return True  #Supposed to return true when num not in Column
            
        
        
            
        if (notInSubGrid(subG, num) and notInRow(rowG, num) and notInColumn(colG, num)):
            # print("Number does not exist in grid or something went wrong but is passes still, \t Can't be bothered to check so it's whatever")
            return True
        else:
            # print("Number already exists in grid")
            return False
        
        
        
        
def userMove(): # Get user move
    while True:
        print("\n Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:", "For example, a move looks like 'B4 9' \n")
        move = input("> ")
        if move[0].upper() == "Q":
            print("Thanks for Playing... \t Goodbye!")
            break
        elif move[0].upper() == "N": 
            dogrid.genNumbs() # again yes yes i knw
            
            dogrid.genBoard()
        # Add conditions for other commands and moves
        else:
            if Utils.validate(move):
                # Update the board based on the user's move
                col = move[0].upper()
                row = int(move[1])
                cell = col + row
                num = int(move[3])
                mainGrid[row - 1][navGrid.index(cell)] = [str(num)]
                dogrid.genBoard()
            else:
                print("Invalid move. Try again.")

# Call the userMove function to start the interaction
userMove()