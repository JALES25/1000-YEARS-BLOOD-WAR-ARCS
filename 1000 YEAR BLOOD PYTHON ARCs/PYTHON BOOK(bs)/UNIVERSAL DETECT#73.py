import random


#region
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



# a  = random.randint(1,9)

# def notInGrid(arr, num):
#     for col in arr:
#         for row in col:
#             for cell in row:
#                 if cell == str(num):
#                     return False
#     return True

# ###############################################################################################
# def validate(placing):
#         subG = []
#         rowG = []
#         colG = []
        
#         def checkPlacing(placing):
#             col = placing[0].upper()
#             row = int(placing[1])
            
#             def assignSubG():
#                 if (col == 'A' and row <= 3) or (col == 'B' and row <= 3) or (col == 'C' and row <= 3):
#                     subG = mainGrid[0]
#                     return subG
#                 elif (col == 'A' and 4 <= row <= 6) or (col == 'B' and 4 <= row <= 6) or (col == 'C' and 4 <= row <= 6):
#                     subG = mainGrid[3]
#                     return subG
#                 elif (col == 'A' and 7 <= row <= 9) or (col == 'B' and 7 <= row <= 9) or (col == 'C' and 7 <= row <= 9):
#                     subG = mainGrid[6]
#                     return subG
                
#                 elif (col == 'D' and row <= 3) or (col == 'E' and row <= 3) or (col == 'F' and row <= 3):
#                     subG = mainGrid[1]
#                     return subG
#                 elif (col == 'D' and 4 <= row <= 6) or (col == 'E' and 4 <= row <= 6) or (col == 'F' and 4 <= row <= 6):
#                     subG = mainGrid[5]
#                     return subG
#                 elif (col == 'D' and 7 <= row <= 9) or (col == 'E' and 7 <= row <= 9) or (col == 'F' and 7 <= row <= 9):
#                     subG = mainGrid[7]
#                     return subG
                    
#                 elif (col == 'H' and row <= 3) or (col == 'I' and row <= 3) or (col == 'J' and row <= 3):
#                     subG = mainGrid[2]
#                     return subG
#                 elif (col == 'H' and 4 <= row <= 6) or (col == 'I' and 4 <= row <= 6) or (col == 'J' and 4 <= row <= 6):
#                     subG = mainGrid[6]
#                     return subG
#                 elif (col == 'H' and 7 <= row <= 9) or (col == 'I' and 7 <= row <= 9) or (col == 'J' and 7 <= row <= 9):
#                     subG = mainGrid[8]
#                     return subG
#             assignSubG()
            
#             def assignRow():
#                 if (row == 1):
#                     rowG.extend([mainGrid[0][0], mainGrid[0][1], mainGrid[0][2], mainGrid[1][0], mainGrid[1][1], mainGrid[1][2], mainGrid[2][0], mainGrid[2][1], mainGrid[2][2]]) 
#             assignRow()
        
#         checkPlacing('A1 9')
#         print(subG) 
        
#         def notInSubGrid(arr, num):
#             for row in arr:
#                 for cell in row:
#                     if cell == str(num):
#                         return False
#             return True
        
#         def notInColumn(arr, num):
            
#             print("TO DO")
            
#         def notInRow(arr, num):
#             print("TO DO")
      
         
        
# validate("A1 9")    
# ###############################################################################################

# # def notInGrid(arr, var):
# #     inGrid = False
# #     for row in arr:
# #         for cell in row:
# #             if cell == var: 
# #                 inGrid = True
# #                 break
# #         if inGrid:
# #             break
# #     return not inGrid  


# def genNumbs():
    
#     def checkEmpty(arr):
#         noEmpty = True
#         for i in range(len(arr)):
#             if not(isinstance(int(arr[i][0]), (int, float))):
#                 noEmpty = False
#         return noEmpty

#     def gensubgrid(arr):
#         while True:
#             for i in range(len(arr)): 
#                 num = random.randint(1,9)
#                 if (num not in arr): 
#                     arr[i][0] = f'{num}'
#             if checkEmpty(arr) == True:
#                 break

#     for i in range(len(mainGrid)):
#         gensubgrid(mainGrid[i])
        
# genNumbs()

# def printGrid():
#     for i in range(len(mainGrid)):
#         print(mainGrid[i])

# printGrid()




# #region
# #######################################################################################
# #######################################################################################
# # Board algos
# class dogrid:
#     # def __init__ (self, subG, rowG, colG):
#     #     self.subG = subG
#     #     self.rowG = rowG
#     #     self.colG = colG
    
#     # subG = []
#     # rowG = []
#     # colG = []
       
#     def checkPlacing(placing) -> object:
#         subG = []
#         rowG = []
#         colG = []
        
#         col = placing[0].upper()
#         print(placing[1])
#         row = int(placing[1])
        
        
#         def assignSubG():
#             if (col == 'A' and row <= 3) or (col == 'B' and row <= 3) or (col == 'C' and row <= 3):
#                 subG = mainGrid[0]
#                 return subG
#             elif (col == 'A' and 4 <= row <= 6) or (col == 'B' and 4 <= row <= 6) or (col == 'C' and 4 <= row <= 6):
#                 subG = mainGrid[3]
#                 return subG
#             elif (col == 'A' and 7 <= row <= 9) or (col == 'B' and 7 <= row <= 9) or (col == 'C' and 7 <= row <= 9):
#                 subG = mainGrid[6]
#                 return subG
            
#             elif (col == 'D' and row <= 3) or (col == 'E' and row <= 3) or (col == 'F' and row <= 3):
#                 subG = mainGrid[1]
#                 return subG
#             elif (col == 'D' and 4 <= row <= 6) or (col == 'E' and 4 <= row <= 6) or (col == 'F' and 4 <= row <= 6):
#                 subG = mainGrid[5]
#                 return subG
#             elif (col == 'D' and 7 <= row <= 9) or (col == 'E' and 7 <= row <= 9) or (col == 'F' and 7 <= row <= 9):
#                 subG = mainGrid[7]
#                 return subG
                
#             elif (col == 'H' and row <= 3) or (col == 'I' and row <= 3) or (col == 'J' and row <= 3):
#                 subG = mainGrid[2]
#                 return subG
#             elif (col == 'H' and 4 <= row <= 6) or (col == 'I' and 4 <= row <= 6) or (col == 'J' and 4 <= row <= 6):
#                 subG = mainGrid[6]
#                 return subG
#             elif (col == 'H' and 7 <= row <= 9) or (col == 'I' and 7 <= row <= 9) or (col == 'J' and 7 <= row <= 9):
#                 subG = mainGrid[8]
#                 return subG    
#         assignSubG()
        
#         def assignRow():
#             if (row == 1):
#                 rowG.extend(mainGrid[0][0], mainGrid[0][1], mainGrid[0][2], mainGrid[1][0], mainGrid[1][1], mainGrid[1][2], mainGrid[2][0], mainGrid[2][1], mainGrid[2][2])
#             elif (row == 2):
#                 rowG.extend(mainGrid[0][3], mainGrid[0][4], mainGrid[0][5], mainGrid[1][3], mainGrid[1][4], mainGrid[1][5], mainGrid[2][3], mainGrid[2][4], mainGrid[2][5])
#             elif (row == 3):
#                 rowG.extend(mainGrid[0][6], mainGrid[0][7], mainGrid[0][8], mainGrid[1][6], mainGrid[1][7], mainGrid[1][8], mainGrid[2][6], mainGrid[2][7], mainGrid[2][8])
                
#             elif (row == 4):
#                 rowG.extend(mainGrid[3][0], mainGrid[3][1], mainGrid[3][2], mainGrid[4][0], mainGrid[4][1], mainGrid[4][2], mainGrid[5][0], mainGrid[5][1], mainGrid[5][2])
#             elif (row == 5):
#                 rowG.extend(mainGrid[3][3], mainGrid[3][4], mainGrid[3][5], mainGrid[4][3], mainGrid[4][4], mainGrid[4][5], mainGrid[5][3], mainGrid[5][4], mainGrid[5][5])
#             elif (row == 6):
#                 rowG.extend(mainGrid[3][6], mainGrid[3][7], mainGrid[3][8], mainGrid[4][6], mainGrid[4][7], mainGrid[4][8], mainGrid[5][6], mainGrid[5][7], mainGrid[5][8])
                
#             elif (row == 7):
#                 rowG.extend(mainGrid[6][0], mainGrid[6][1], mainGrid[6][2], mainGrid[7][0], mainGrid[7][1], mainGrid[7][2], mainGrid[8][0], mainGrid[8][1], mainGrid[8][2])
#             elif (row == 8):
#                 rowG.extend(mainGrid[6][3], mainGrid[6][4], mainGrid[6][5], mainGrid[7][3], mainGrid[7][4], mainGrid[7][5], mainGrid[8][3], mainGrid[8][4], mainGrid[8][5])
#             elif (row == 9):
#                 rowG.extend(mainGrid[6][6], mainGrid[6][7], mainGrid[6][8], mainGrid[7][6], mainGrid[7][7], mainGrid[7][8], mainGrid[8][6], mainGrid[8][7], mainGrid[8][8])
#         assignRow()
        
#         def assignCol():
#             if (col == 'A'):
#                 colG.extend([mainGrid[0][0], mainGrid[0][3], mainGrid[0][6], mainGrid[3][0], mainGrid[3][3], mainGrid[3][6], mainGrid[6][0], mainGrid[6][3], mainGrid[6][6]])
#             elif (col == 'B'):
#                 colG.extend([mainGrid[0][1], mainGrid[0][4], mainGrid[0][7], mainGrid[3][1], mainGrid[3][4], mainGrid[3][7], mainGrid[6][1], mainGrid[6][4], mainGrid[6][7]])
#             elif (col == 'C'):
#                 colG.extend([mainGrid[0][2], mainGrid[0][5], mainGrid[0][8], mainGrid[3][2], mainGrid[3][5], mainGrid[3][8], mainGrid[6][2], mainGrid[6][5], mainGrid[6][8]])
            
#             elif (col == 'D'):
#                 colG.extend([mainGrid[1][0], mainGrid[1][3], mainGrid[1][6], mainGrid[4][0], mainGrid[4][3], mainGrid[4][6], mainGrid[7][0], mainGrid[7][3], mainGrid[7][6]])
#             elif (col == 'E'):
#                 colG.extend([mainGrid[1][1], mainGrid[1][4], mainGrid[1][7], mainGrid[4][1], mainGrid[4][4], mainGrid[4][7], mainGrid[7][1], mainGrid[7][4], mainGrid[7][7]])
#             elif (col == 'F'):
#                 colG.extend([mainGrid[1][2], mainGrid[1][5], mainGrid[1][8], mainGrid[4][2], mainGrid[4][5], mainGrid[4][8], mainGrid[7][2], mainGrid[7][5], mainGrid[7][8]])
            
#             if (col == 'G'):
#                 colG.extend([mainGrid[2][0], mainGrid[2][3], mainGrid[2][6], mainGrid[5][0], mainGrid[5][3], mainGrid[5][6], mainGrid[8][0], mainGrid[8][3], mainGrid[8][6]])
#             elif (col == 'H'):
#                 colG.extend([mainGrid[2][1], mainGrid[2][4], mainGrid[2][7], mainGrid[5][1], mainGrid[5][4], mainGrid[5][7], mainGrid[8][1], mainGrid[8][4], mainGrid[8][7]])
#             elif (col == 'I'):
#                 colG.extend([mainGrid[2][2], mainGrid[2][5], mainGrid[2][8], mainGrid[5][2], mainGrid[5][5], mainGrid[5][8], mainGrid[8][2], mainGrid[8][5], mainGrid[8][8]])
#         assignCol()

#         placingObj = object()
#         placingObj.subG = subG
#         placingObj.rowG = rowG
#         placingObj.colG = colG
        
#         return placingObj
#     # checkPlacing(placing)

    
#     def validate(placing):
#         placings = dogrid.checkPlacing(placing)
#         subG = placings.subG
#         rowG = placings.rowG
#         colG = placings.colG
        
#         col = placing[0].upper()
#         row = int(placing[1])
#         num = int(placing[3])
        
#         def notInSubGrid(arr, num): 
#             for row in arr:
#                 for cell in row:
#                     if cell == str(num):
#                         return False
#             return True
        
#         def notInColumn(arr, num):
#             for row in arr:
#                 for cell in row:
#                     if cell == str(num):
#                         return False
#             return True
            
#         def notInRow(arr, num):
#             for row in arr:
#                 for cell in row:
#                     if cell == str(num):
#                         return False
#             return True
            
#         if (notInSubGrid(subG, num) and notInRow(rowG, num) and notInColumn(colG, num)):
#             print("Number exists in grid")
#             return True
#         else:
#             print("Number does not exist in grid")
#             return False
            
    
#     def genNumbs():
        
#         def checkEmpty(arr):
#             noEmpty = True
#             for i in range(len(arr)):
#                 if not(isinstance(int(arr[i][0]), (int, float))):
#                     noEmpty = False
#             return noEmpty

#         def gensubgrid(arr):
#             while True:
#                 for i in range(len(arr)): 
#                     num = random.randint(1,9)
#                     if (str(num) not in arr): 
#                         arr[i][0] = f'{num}'
#                 if checkEmpty(arr) == True:
#                     break
        
#         # i want to iterate through the mainGrid and the navGrid so that the dogrid.validate() gets the co-ordinates of cell 
#         def gengrid(arr1, arr2):
#             while True:
#                 for index, (arr1, arr2) in enumerate(zip(arr1, arr2)):
#                     num = random.randint(1,9)
#                     if (dogrid.validate(arr2)): #nothing like a 40 min rant/tantrun to then say no theres a better way 
#                         arr1[index][0] = f'{num}'
#                 if checkEmpty(arr1) == True:
#                     break
         

#         for i in range(len(mainGrid)):
#             # gensubgrid(mainGrid[i])
#             gengrid(mainGrid, navGrid)
            
    
    
#     # Algo to Display the Soduku Board
#     def genBoard(): 
#         outputBoard = "\n"
        
#         outputBoard += lTop + "\n"
#         rowNum = 0
        
#         for i in range(0,9,3): # First subgrid row
#             outputBoard += f"{rowNum+1} {mainGrid[0][i]}{mainGrid[0][i+1]}{mainGrid[0][i+2]} {vfillSpace} {mainGrid[1][i]}{mainGrid[1][i+1]}{mainGrid[1][i+2]} {vfillSpace} {mainGrid[2][i]}{mainGrid[2][i+1]}{mainGrid[2][i+2]} \n"
#             rowNum += 1
            
#         outputBoard += hfillSpace + "\n"
        
#         for i in range(0,9,3): # Second subgrid row
#             outputBoard += f"{rowNum+1} {mainGrid[3][i]}{mainGrid[3][i+1]}{mainGrid[3][i+2]} {vfillSpace} {mainGrid[4][i]}{mainGrid[4][i+1]}{mainGrid[4][i+2]} {vfillSpace} {mainGrid[5][i]}{mainGrid[5][i+1]}{mainGrid[5][i+2]} \n"
#             rowNum += 1
        
#         outputBoard += hfillSpace + "\n"
#         subGrid9[i+2] = [f'{9}']
#         for i in range(0,9,3): # Third subgrid row
#             outputBoard += f"{rowNum+1} {mainGrid[6][i]}{mainGrid[6][i+1]}{mainGrid[6][i+2]} {vfillSpace} {mainGrid[7][i]}{mainGrid[7][i+1]}{mainGrid[7][i+2]} {vfillSpace} {mainGrid[8][i]}{mainGrid[8][i+1]}{mainGrid[8][i+2]} \n"
#             rowNum += 1

#         print("--snip--")
#         print(outputBoard)
#         print("--snip--")
    
 
# #######################################################################################
# #endregion


# def doSom(arr1,arr2):
#     for index, (arr1, arr2) in enumerate(zip(arr1, arr2)):
#         num = random.randint(1,9)
#         if (dogrid.validate(arr2)): #nothing like a 40 min rant/tantrun to then say no theres a better way 
#             arr1[index][0] = f'{num}'
            
# doSom(mainGrid, '')

# a = [['7'], ['5'], ['1'], ['7'], ['7'], ['9'], ['8'], ['8'], ['1']]

# def notInSubGrid(arr, num): 
#     for row in arr:
#         for cell in row:
#             if cell == str(num):
#                 return False
#     return True  #Supposed to return true when num not in subGrid

# print(notInSubGrid(a, 2), "This works")
        
# def notInColumn(arr, num):
#     for row in arr:
#         for cell in row:
#             if cell == str(num):
#                 return False
#     return True  #Supposed to return true when num not in Column
 
# print(notInColumn(a, 2), "This works") 
    
# def notInRow(arr, num):
#     for row in arr:
#         for cell in row:
#             if cell == str(num):
#                 return False
#     return True  #Supposed to return true when num not in Row
# ############################TEST CASES SECTION#########################################



 
# # print(notInGrid(mainGrid,6))
# # print(notInGrid(mainGrid,7))
# # print(notInGrid(mainGrid,"*"))
# # print(notInGrid(mainGrid,9))
# # print(notInGrid(mainGrid,'-'))
# # print(notInGrid(mainGrid,5))
# # print(notInGrid(mainGrid,2))

# # print("\n")
# # a1 = [[["1"],["2"],[3],[4],["5"],["-"],["-"],["-"],["-"]],[["1"],["2"],[3],[4],["5"],["-"],["-"],["-"],["-"]],[["1"],["2"],[3],[4],["5"],["-"],["-"],["-"],["-"]]]
# # print(notInGrid(a1,3))
# # print(notInGrid(a1,4))

# # print("\n")
# # a1 = [[1],[2],[3],[4],["5"]]
# # print(notInGrid(a1,3))
# # print(notInGrid(a1,4))
# # print(notInGrid(a1,5))

#endregion




########################################################################################################################

class doGrid:
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

########################################################################################################################
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
########################################################################################################################
########################################################################################################################


#region  - alt algo
def initializeBoard():
    # Initialize the board with some given values
    mainGrid[0][0] = ['5']
    mainGrid[0][3] = ['3']
    mainGrid[1][1] = ['6']
    mainGrid[1][4] = ['7']
    mainGrid[1][5] = ['9']
    mainGrid[2][2] = ['8']
    mainGrid[2][7] = ['6']
    mainGrid[3][0] = ['8']
    mainGrid[4][2] = ['4']
    mainGrid[5][5] = ['3']
    mainGrid[5][8] = ['1']
    mainGrid[6][1] = ['7']
    mainGrid[6][6] = ['9']
    mainGrid[7][4] = ['5']
    mainGrid[7][5] = ['1']
    mainGrid[8][3] = ['3']
    mainGrid[8][8] = ['8']

# Call initializeBoard to set the initial values
initializeBoard()


def gensubgrid(arr):
    # Generate Sudoku numbers for a 3x3 subgrid
    nums = random.sample(range(1, 10), 9)
    for i in range(len(arr)):
        arr[i][0] = [str(nums[i])]



def checkEmpty(main_grid):
    for subgrid in main_grid:
        if any(cell == ["-"] for row in subgrid for cell in row):
            return True
    return False


def validate(placing):
    # Get the subgrid, row, and column for the placement
    placingObj = doGrid.checkPlacing(placing)
    subG = placingObj["subG"]
    rowG = placingObj["rowG"]
    colG = placingObj["colG"]
    
    col = placing[0].upper()
    row = int(placing[1])
    num = int(placing[3]) if len(placing) > 2 else None

    if num is None:
        print("Number to check not given or something went wrong. Can't be bothered to check, so it's whatever.")
        return False

    def notInSubGrid(arr, num):
        for row in arr:
            for cell in row:
                if cell == str(num):
                    return False
        return True

    def notInColumn(arr, num):
        for row in arr:
            for cell in row:
                if cell == str(num):
                    return False
        return True

    def notInRow(arr, num):
        for row in arr:
            for cell in row:
                if cell == str(num):
                    return False
        return True

    

    if not (notInSubGrid(subG, num) and notInRow(rowG, num) and notInColumn(colG, num)):
        print("Number already exists in grid.")
        return False

    print("Placement is valid.")
    return True


def genBoard():
    outputBoard = "\n"
    outputBoard += "    A    B    C         D    E    F         G    H    I\n"
    for i, row in enumerate(mainGrid):
        outputBoard += f"{i + 1} "
        for subgrid in row:
            outputBoard += f"{subgrid[0][0]}    "
        outputBoard = outputBoard.rstrip() + "\n"
        if (i + 1) % 3 == 0 and i != 8:
            outputBoard += "  ---------------     ---------------     ---------------\n"
    print(outputBoard)


def gengrid(arr1, arr2):
    while True:
        for index, (arr1, arr2) in enumerate(zip(arr1, arr2)):
            for place, key in zip(arr1, arr2):
                num = random.randint(1, 9)
                placing = f'{key} {num}'
                if validate(placing):
                    place[0] = placing[3]
                    
        if not checkEmpty(arr1):
            break

genBoard()


def genNumbs():
    # Generate Sudoku numbers for each 3x3 subgrid
    for subgrid in mainGrid:
        gensubgrid(subgrid)

# Call genNumbs to generate initial Sudoku numbers
genNumbs()





def userMove():
    while True:
        move = input("Enter a move (e.g., 'B4 9'), RESET, NEW, UNDO, ORIGINAL, or QUIT: ")
        if move.upper() == "QUIT":
            print("Goodbye!")
            break
        elif move.upper() == "NEW":
            initializeBoard()
            genNumbs()
            genBoard()
        # Add conditions for other commands and moves
        else:
            if validate(move):
                col = move[0].upper()
                row = int(move[1])
                num = int(move[3])
                mainGrid[row - 1][navGrid.index(col)] = [str(num)]
                genBoard()
            else:
                print("Invalid move. Try again.")





userMove()



#endregion