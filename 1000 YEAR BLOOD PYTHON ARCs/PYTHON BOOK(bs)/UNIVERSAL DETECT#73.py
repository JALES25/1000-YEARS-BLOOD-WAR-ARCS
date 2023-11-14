import random
# arr = [['-'],[],[],[],[],[],[],[],[]]
#####################################################################
subGrid1 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid2 = [["-"],["-"],["-"],["-"],["-"],["7"],["-"],["-"],["-"]]
subGrid3 = [["-"],["-"],["3"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid4 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid5 = [["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid6 = [["6"],["-"],["-"],[5],["-"],["-"],["-"],["-"],["-"]]
subGrid7 = [["-"],["-"],["-"],["-"],["4"],["-"],["5"],["-"],["-"]]
subGrid8 = [["-"],["-"],["1"],["-"],["-"],["-"],["-"],["-"],["-"]]
subGrid9 = [["-"],["5"],["-"],["-"],["-"],["-"],["-"],["-"],["9"]]

mainGrid = [[*subGrid1],[*subGrid2],[*subGrid3],[*subGrid4],[*subGrid5],[*subGrid6],[*subGrid7],[*subGrid8],[*subGrid9]]
#####################################################################

a  = random.randint(1,9)

def notInGrid(arr, num):
    for col in arr:
        for row in col:
            for cell in row:
                if cell == str(num):
                    return False
    return True

###############################################################################################
def validate(placing):
        subG = []
        rowG = []
        colG = []
        
        def checkPlacing(placing):
            col = placing[0].upper()
            row = int(placing[1])
            
            def assignSubG():
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
            assignRow()
        
        checkPlacing('A1 9')
        print(subG) 
        
        def notInSubGrid(arr, num):
            for row in arr:
                for cell in row:
                    if cell == str(num):
                        return False
            return True
        
        def notInColumn(arr, num):
            
            print("TO DO")
            
        def notInRow(arr, num):
            print("TO DO")
      
         
        
validate("A1 9")    
###############################################################################################

# def notInGrid(arr, var):
#     inGrid = False
#     for row in arr:
#         for cell in row:
#             if cell == var: 
#                 inGrid = True
#                 break
#         if inGrid:
#             break
#     return not inGrid  


def genNumbs():
    
    def checkEmpty(arr):
        noEmpty = True
        for i in range(len(arr)):
            if not(isinstance(int(arr[i][0]), (int, float))):
                noEmpty = False
        return noEmpty

    def gensubgrid(arr):
        while True:
            for i in range(len(arr)): 
                num = random.randint(1,9)
                if (num not in arr): 
                    arr[i][0] = f'{num}'
            if checkEmpty(arr) == True:
                break

    for i in range(len(mainGrid)):
        gensubgrid(mainGrid[i])
        
genNumbs()

def printGrid():
    for i in range(len(mainGrid)):
        print(mainGrid[i])

printGrid()
    
# print(notInGrid(mainGrid,6))
# print(notInGrid(mainGrid,7))
# print(notInGrid(mainGrid,"*"))
# print(notInGrid(mainGrid,9))
# print(notInGrid(mainGrid,'-'))
# print(notInGrid(mainGrid,5))
# print(notInGrid(mainGrid,2))

# print("\n")
# a1 = [[["1"],["2"],[3],[4],["5"],["-"],["-"],["-"],["-"]],[["1"],["2"],[3],[4],["5"],["-"],["-"],["-"],["-"]],[["1"],["2"],[3],[4],["5"],["-"],["-"],["-"],["-"]]]
# print(notInGrid(a1,3))
# print(notInGrid(a1,4))

# print("\n")
# a1 = [[1],[2],[3],[4],["5"]]
# print(notInGrid(a1,3))
# print(notInGrid(a1,4))
# print(notInGrid(a1,5))