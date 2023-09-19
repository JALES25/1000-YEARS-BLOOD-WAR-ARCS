""" If you are of a certain age, you'll remember those ancient technological devices called DVD plsyers.
    When not playing DVDs, they would display a diagonally travelling DVD logo that bounced off the edges of a screen.
    This program simulates this colorfull DVD logo by making it change direction each time it hits an edge.
    we'll also keep track of how many times a logo hits a corner of a screen.
    This creates an interesting visual animation to look at, especially for the magical moment
    when a logo lines up perfectly with a corner.
    RUN THROUGH TERMINAL """

""" The bext module's goto() function works the same way: Calling bext.goto(0,0) places the cursor at the top left of
    the terminal window. We represent each bouncing DVD logo using a python dictionary with the keys 'color' , 'direction',
    'x' and 'y'. The values for the 'x' and 'y' are integers representing the logo's position in the window. 
    Since these values get passed to bext.goto(), increasing them will move the logo right and down,
    while decreasing them will move the logo left and up. """

import sys, random, time


try:
    import bext
except ImportError:
    print("This program requires the bext module to run!")
    sys.exit()


#Set up the constants:
WIDTH, HEIGHT = bext.size()
""" #We can't print to the last column on Windows without it adding a newline automatically, so reduce the width by one: """
WIDTH -= 1

NUMBER_OF_LOGOS = 5 # (!) Change me T-T
PAUSE_AMOUNT = 0.2  # (!) Change me T-T
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"] # (!) Change me T-T

UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

#Key names for logo dictionaries:
COLOR = "color"
X = "x"
Y = "y"
DIR = "direction"

def main():
    bext.clear()

    #Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS), 
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)}) 

        if logos[-1][X] % 2 == 1:
            #Make sure x is even so it can hit the corner.
            logos [-1][X] -= 1
    
    cornerBounces = 0 #Count how many times a logo hits a corner.
    while True: #Main program loop.
        for logo in logos: #Handle each logo in the logos list.
            #Erase the logo's current location:
            bext.goto(logo[X], logo[Y])

            print("    ", end="") # T-T

            originalDirection = logo[DIR]

            #See if the logo bounces of the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT # (>_0) goods odds amirite
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH -3 and logo[Y] == - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            #See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            
            #See if the logo bounces off the right edge:
            #(WIDTH - 3 cuz DVD has 3 Ls.)
            elif logo[X] ==  WIDTH -3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            #See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] == DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] == DOWN_RIGHT

            #See if the logos bounces off the bottom edge:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                #Change color when the logo bounces:
                logo[COLOR] = random.choice(COLORS)

            #Move the logo. (X moves by 2 because the terminal characters are twice as tall as they are wide.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
        
        #Display number of corner bounces:
        bext.goto(5,0)
        bext.fg("white")
        print("corner bounces:", cornerBounces, end="")

        for logo in logos:
            #Draw te logos at their new location:
            bext.goto(logo[X], logo[Y],)
            bext.fg(logo[COLOR])
            print("DVD", end="")
        
        bext.logo(0,0)

        sys.stdout.flush() #(Required for bext-using programs.)
        time.sleep(PAUSE_AMOUNT)


#If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing DVD Logo, COPY COPY COPY")
        sys.exit() #When Ctrl-C is pressed, end the program. 




intro =""" Bouncing DVD Logo COPY COPY COPY 
        A bouncing DVD logo animation. Yus hav to b "of a certain age" to appreciate this. 
        Press Ctrl-C to stop. """
