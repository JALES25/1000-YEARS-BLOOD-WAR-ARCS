""" Sudoku is a popular puzzle game in news-papers and mobile apps. 
    The Sudoku board is a 9 × 9 grid in which the player must place the digits 1 to 9 once, 
    and only once, in each row, column, and 3 × 3 subgrid. 
    The game begins with a few spaces already filled in with digits, called givens. 
    A well-formed Sudoku puzzle will have only one possible valid solution."""
 
import random
import time
import copy
   
print("Welcome to Soduku Puzzle, by TYLONs17", "\n")

####### TODO: 
#   add way to manipulate the number of empty cells in the board (difficulty adjustments) --in progress--
#   add way to determine win / lose conditions
#

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


# Another Main Grid (bruh) 
sudoku_board = [[["-"] for _ in range(9)] for _ in range(9)]

# Board algos
class dogrid:
    # def __init__ (self, mainGrid, subG, rowG, colG):
    #     self.maingrid = mainGrid
    #     self.subG = subG
    #     self.rowG = rowG
    #     self.colG = colG
    
    
    
        # Algo to Display the Soduku Board
    def genBoard(grid): 
        outputBoard = "\n"
        
        outputBoard += lTop + "\n"
        rowNum = 0
        
        for i in range(0,9,3): # First subgrid row
            outputBoard += f"{rowNum+1} {grid[0][i]}{grid[0][i+1]}{grid[0][i+2]} {vfillSpace} {grid[1][i]}{grid[1][i+1]}{grid[1][i+2]} {vfillSpace} {grid[2][i]}{grid[2][i+1]}{grid[2][i+2]} \n"
            rowNum += 1
            
        outputBoard += hfillSpace + "\n"
        
        for i in range(0,9,3): # Second subgrid row
            outputBoard += f"{rowNum+1} {grid[3][i]}{grid[3][i+1]}{grid[3][i+2]} {vfillSpace} {grid[4][i]}{grid[4][i+1]}{grid[4][i+2]} {vfillSpace} {grid[5][i]}{grid[5][i+1]}{grid[5][i+2]} \n"
            rowNum += 1
        
        outputBoard += hfillSpace + "\n"
        
        # subGrid9[i+2] = [f'{9}'] # Don mind me im just existing for testing 
        for i in range(0,9,3): # Third subgrid row
            outputBoard += f"{rowNum+1} {grid[6][i]}{grid[6][i+1]}{grid[6][i+2]} {vfillSpace} {grid[7][i]}{grid[7][i+1]}{grid[7][i+2]} {vfillSpace} {grid[8][i]}{grid[8][i+1]}{grid[8][i+2]} \n"
            rowNum += 1

        print("--snip--")
        print(outputBoard)
        print("--snip--")


    # Algo to empty cells
    def emptyCells(grid, num_empty_cells):
        # Flatten the grid to a list of cell coordinates
        cell_coords = [(i, j) for i in range(9) for j in range(9)]
        
        # Randomly shuffle the cell coordinates
        random.shuffle(cell_coords)
        
        # Empty the desired number of cells
        for i in range(num_empty_cells):
            x, y = cell_coords[i]
            grid[x][y] = ["-"]

        return grid
    
       
    def checkPlacing(placing, mainGrid = mainGrid):
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
        # col_index = ord(placing[0].upper()) - ord('A')
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
     
     
     
    def checkEmpty(main_grid):
            """
            Check if the main grid contains any cell with the value ["-"]. Which represents th default empty value
            """
            for subgrid in main_grid:
                if any(cell == ["-"] for row in subgrid for cell in row):
                    return True  # If any cell with value ["-"] is found, return True
                
            # for i in range(len(main_grid)):
            #     if not(isinstance(int(main_grid[i][0]), (int, float))):
            #         return False
            #     return True 

            return False  # If no such cell is found, return False    
        
    
    def genNumbs():
        
        # i want to iterate through the mainGrid and the navGrid so that the dogrid.validate() gets the co-ordinates of cell 
        def gengrid(arr1, arr2):
            while True:
                for index, (arr1_item, arr2_item) in enumerate(zip(arr1, arr2)):
                    
                    for place, key in zip(arr1_item, arr2_item):
                        num = random.randint(1,9)
                        placing = f'{key} {num}'

                        if dogrid.validate(placing): # TODO: also needs to check if the current cell is empty
                            place[0] = placing[3]
                       
                    # placing = f'{arr2[index]} {num}'
                    # if (dogrid.validate(placing)): # nothing like a 40 min rant/tantrun to then say no theres a better way 
                    #     arr1[index][0] = f'{num}'
                        
                # dogrid.genBoard(mainGrid)
                    
                

                if dogrid.checkEmpty(arr1) == False:
                    break
         

        for i in range(len(mainGrid)):
            # gensubgrid(mainGrid[i])
            gengrid(mainGrid, navGrid)
            
    
   
   
   
# Utils   
class Utils: 
    def getBoard(grid): 
        outputBoard = "\n"
        
        outputBoard += lTop + "\n"
        rowNum = 0
        
        for i in range(0,9,3): # First subgrid row
            outputBoard += f"{rowNum+1} {grid[0][i]}{grid[0][i+1]}{grid[0][i+2]} {vfillSpace} {grid[1][i]}{grid[1][i+1]}{grid[1][i+2]} {vfillSpace} {grid[2][i]}{grid[2][i+1]}{grid[2][i+2]} \n"
            rowNum += 1
            
        outputBoard += hfillSpace + "\n"
        
        for i in range(0,9,3): # Second subgrid row
            outputBoard += f"{rowNum+1} {grid[3][i]}{grid[3][i+1]}{grid[3][i+2]} {vfillSpace} {grid[4][i]}{grid[4][i+1]}{grid[4][i+2]} {vfillSpace} {grid[5][i]}{grid[5][i+1]}{grid[5][i+2]} \n"
            rowNum += 1
        
        outputBoard += hfillSpace + "\n"
        
        # subGrid9[i+2] = [f'{9}'] # Don mind me im just existing for testing 
        for i in range(0,9,3): # Third subgrid row
            outputBoard += f"{rowNum+1} {grid[6][i]}{grid[6][i+1]}{grid[6][i+2]} {vfillSpace} {grid[7][i]}{grid[7][i+1]}{grid[7][i+2]} {vfillSpace} {grid[8][i]}{grid[8][i+1]}{grid[8][i+2]} \n"
            rowNum += 1

        # print("--snip--")
        # print(outputBoard)
        # print("--snip--")
        
        return outputBoard
    
    def validate(placing):
        placings = dogrid.checkPlacing(placing)
        subG = placings["subG"]
        rowG = placings["rowG"]
        colG = placings["colG"]

        col_index = ord(placing[0].upper()) - ord('A')
        row = int(placing[1])
        num = int(placing[3]) if len(placing) == 4 else None

        if num is None:
            return False

        def notInSubGrid(arr, num):
            # Extract the subgrid
            subgrid = [row[col_index * 3:(col_index + 1) * 3] for row in arr[row // 3 * 3:(row // 3 + 1) * 3]]
            return num not in [cell for row in subgrid for cell in row]

        def notInColumn(arr, num):
            return num not in [row[col_index] for row in arr]

        def notInRow(arr, num):
            return num not in [cell for cell in arr[row]]

        return notInSubGrid(subG, num) and notInRow(rowG, num) and notInColumn(colG, num)

    def validateMove(move, mainGrid = mainGrid):
        placings = dogrid.checkPlacing(move, mainGrid)
        subG = placings["subG"]
        # print(subG)
        rowG = placings["rowG"]
        # print(rowG)
        colG = placings["colG"]
        # print(colG)
        
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
                        print("check3 - \t number exists in the column")
                        return False
            return True  #Supposed to return true when num not in Column
            
        
        
            
        if (notInSubGrid(subG, num) and notInRow(rowG, num) and notInColumn(colG, num)): # TODO || This check needs proper implemetation or refactoring, currently not suitable as a validation to generate a valid grid
            # print("Number does not exist in grid or something went wrong but is passes still, \t Can't be bothered to check so it's whatever")
            return True # If the number is not in the subgrid, row and column then allow the number to be inserted
        else:
            # print("Number already exists in grid")
            return False
        
     
    # Algo for puzzle dificulty
    def generate_puzzle(difficulty):
        dogrid.genNumbs()
    
        if difficulty == 'easy':
            num_empty_cells = random.randint(20, 30)
        elif difficulty == 'medium':
            num_empty_cells = random.randint(31, 45)
        elif difficulty == 'hard':
            num_empty_cells = random.randint(46, 60)
        else:  # very hard
            num_empty_cells = random.randint(61, 81)

        dogrid.emptyCells(mainGrid, num_empty_cells)

        return mainGrid   
        
        
    def getNavIndex(cellToFind): 
        for subgrid in navGrid:
            # print(subgrid)
            for cell in subgrid:
                # print(cell)
                if cell == cellToFind:
                    return subgrid.index(cell)
        return None  # return nothing if the cell isn't found
    
        
        # for subgrid in navGrid:
        #         if any(cell0 == cell for row in subgrid for cell0 in row):
        #             return subgrid.index(cell)  # If any cell with matching value in cell is found, get the index
        
        
def userMove(): # Get user move
    while True:
        print("\n Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:", "For example, a move looks like 'B4 9' \n")
        move = input("> ")
        if move[0].upper() == "Q":
            print("Thanks for Playing... \t Goodbye!")
            break
        elif move[0].upper() == "N": 
            dogrid.genNumbs() # again yes yes i knw
            
            dogrid.genBoard(mainGrid)
        else:
            if Utils.validateMove(move):
                # Update the board based on the user's move
                col = move[0].upper()
                row = int(move[1])
                cell = col + str(row)
                num = int(move[3])
                
                navIndex = Utils.getNavIndex(cell)
                
                    
                mainGrid[row - 1][navIndex] = [str(num)]
                if mainGrid[row - 1][navIndex] == num:
                    print(f"Placed the number {num} on cell {cell}")
                else:
                    print("OHhhh No!!! \t Couldn't place the number something went wrong!!")
                dogrid.genBoard(mainGrid)
            else:
                print("Invalid move. Try again.")

   




#################################################
#################################################
#################################################
#################################################
#################################################

# print(Utils.getNavIndex("C2"))

# # Generate the grid
# dogrid.genNumbs()  # -- yes yes i knw

# # Display the grid  
# dogrid.genBoard(mainGrid)


# print("--Here we go")
# Utils.generate_puzzle("medium")
# dogrid.genBoard(mainGrid)
# # Call the userMove function to start the interaction
# userMove()







""" Romaticism isn't real

        ....(Fantasy - Mariah Carey) - the bg sounds and mood setting
             
        she was into this idea of me from her delusioned hopes and dreams
        i got to see her disapointed at that incomplete version of me
        it didn't matter, did it
        i thought she liked me, oh how the world could turn oh so morbid
        Flikkrd an already timid soul.. cold, cold, cold.
        
        everything went quiet for me
        i could only hear the sound and vibration of my heart beating,
        soon after the faint sound of my own distorted breathing.... 
        the next thing i knew 
        
        get out my fkn face
        i flkkrd into JAQUE, i am all smiles
        coinsidental monster, nightmarish menace
        
        .....
        
        "hopefully i could find my mind coz i've lost somewhere along the way
        and i pray that you could find some time coz there's only so many minutes in the day
        come sink with me into the abyss, i'm looking forward to making memories to reminise" - Justin B (Everything)
        
"""

class Romaticism:
    chosenDif = False
    game_states = [] # State manegement in python just as in React ;)
    
    def generate_sudoku(self):    
        
        def is_valid(board, row, col, num):
            # Check if the number is not in the same row, column, or 3x3 subgrid
            return (
                [str(num)] not in board[row] and
                [str(num)] not in [board[i][col] for i in range(9)] and
                [str(num)] not in [board[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3)]
            )

        def solve(board): # Algo to fill the board
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ["-"]:
                        for num in range(1, 10):
                            if is_valid(board, i, j, num):
                                board[i][j] = [str(num)]
                                if solve(board):
                                    return True
                                board[i][j] = ["-"]
                        return False
            return True
        
        solve(sudoku_board)

        return sudoku_board
    
    
    # Remove some numbers to create the puzzle
    def empty_cells(self, grid, num_empty_cells):
        for _ in range(num_empty_cells):
            row, col = random.randint(0, 8), random.randint(0, 8)
            grid[row][col] = ['-']
            
    # Algo for puzzle dificulty
    def adjust_difficulty(self, grid):
        print("Enter Sudoku board difficulty, EASY, MEDIUM, HARD.")
        difficulty = input("> ") 
        print(f"\t You have selected {difficulty.upper()} difficulty. \n")

        if difficulty.upper() == 'EASY':
            num_empty_cells = random.randint(20, 30)
        elif difficulty.upper() == 'MEDIUM':
            num_empty_cells = random.randint(31, 45)
        elif difficulty.upper() == 'HARD':
            num_empty_cells = random.randint(46, 60)
        else:  # very hard (I am a manace)
            num_empty_cells = random.randint(61, 81)

        self.empty_cells(grid, num_empty_cells)

        return grid


    def userMove(self): # Get user move
        while True:
            sudoku_grid = self.generate_sudoku()
            
            
            #     dogrid.genBoard(sudoku_grid)
            #     self.chosenDif = True
            time.sleep(3)
            
            if self.chosenDif == False:
                self.adjust_difficulty(sudoku_grid)
                self.chosenDif = True
                
                time.sleep(2)
            
                dogrid.genBoard(sudoku_grid)
            
            
                
            time.sleep(3)
            
            print("\n Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:", "For example, a move looks like 'B4 9' \n")
            # TODO -Add RESET, UNDO and ORIGINAL functionality
            move = input("> ")
            if move[0].upper() == "Q":
                print("Thanks for Playing... \t Goodbye!")
                break
            elif move[0].upper() == "N":       
                print("Staring a new game please wait...")
                time.sleep(5)
                
                self.adjust_difficulty(sudoku_grid)
                dogrid.genBoard(sudoku_grid)
                
                # Romaticism.userMove() # Recursion on user inputs. must comply
            elif move[0].upper() == "U":
                if self.game_states:
                    sudoku_grid = self.game_states.pop()
                    dogrid.genBoard(sudoku_grid)
                else:
                    print("No Need, You didn't make a Move yet to undo.")
            else:
                if Utils.validateMove(move, sudoku_grid):
                    self.game_states.append(copy.deepcopy(sudoku_grid))
                    
                    # Update the board based on the user's move
                    col = move[0].upper()
                    row = int(move[1])
                    cell = col + str(row)
                    num = int(move[3])
                    
                    navIndex = Utils.getNavIndex(cell)
                    
                    print(sudoku_grid[row - 1][navIndex])  
                    sudoku_grid[row - 1][navIndex] = [str(num)]
                    print(sudoku_grid[row - 1][navIndex])
                    if sudoku_grid[row - 1][navIndex] == [str(num)]:
                        time.sleep(2)
                        print(f"\t Placed the number {num} on cell {cell} \n")
                    else:
                        time.sleep(8)
                        print("OHhhh No!!! \t Couldn't place the number something went wrong!!")
                        
                    time.sleep(4)
                    dogrid.genBoard(sudoku_grid)
                else:
                    print("Invalid move. Try again.")



sudoku_game = Romaticism()
sudoku_game.userMove()  







