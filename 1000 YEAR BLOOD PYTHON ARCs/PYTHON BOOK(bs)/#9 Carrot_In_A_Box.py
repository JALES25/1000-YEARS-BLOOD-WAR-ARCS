"""This is a simple and silly bluffing game for two human players. 
    Each player has a box.
    One box has a carrot int it, and each player wants to have the carrot. 
    The first player looks into their box and the tells the second player they either do or don't have the carrot.
    The second player gets to decide whether to swap boxes or not.
    """


print("Carrot in a Box, by TYLONs") 
print("--snip--")

player1 = input("Human player 1, Enter your name: ")
player2 = input("Human player 2, Enter your name: ")

print("HERE ARE TWO BOXES:")

boxes = """
  __________        ___________
 /         /|      /          /|
+---------+ |     +----------+ |
|  BLACK  | |     |   White  | |
|  BOX    | /     |  BOX     | /
+---------+/      +----------+/
player1             player2

"""

print(player1, " You have a BLACK BOX in front of you.")
print(player2, " You have a WHITE BOX in front of you.")

print("\nPress Enter to continue...\n")

print("---snip---")
print("When Bob has closed their eyes, press Enter...")
print("Alice here is the inside of your box:")

