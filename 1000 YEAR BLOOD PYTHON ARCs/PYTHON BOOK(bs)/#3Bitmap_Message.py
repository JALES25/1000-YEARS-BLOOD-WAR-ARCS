"""This progarm uses a multyline string as a bitmap, a 2D image with only two possible colors for each pixel,
    to determine how it should display a message from the user. In this bitmap, space characters represent an empty space,
    and all other characters are replaced by characters in the user's message. The provided bitmap resembles a world map,
    but you can change this to any image you'd like. The binary simplicity of the space-or-message-characters system
    makes it good for biginers. Try experimenting with different messages to see what the results looks like!"""

import sys

print("Bitmap message, by TYLONs")
print()

#_____________________________________________________________________________________________________________________

""" Wanted to write code to draw the actual map with the users input message T-T. come back n do so """
""" 
print("Enter the message to display with the bitmap.")
print()

#binp = input("> ")
#binp.append(!)
#print(binp)
inp = "Hello!"
legen = ""
spc = " "

while len(legen) <= 68:
    legen += inp

leg = ""
while len(leg) <= 81:
    for index1, elemA in enumerate(inp):
        leg += elemA[index1]
print(leg)
print(legen)
#print((binp+"!") * 12)

print(legen)#topL

print((spc * 3))#1
print()#2
print()#3
print()#4
print()#4
print()#5
print()#6
print()#7
print()#8
print()#9
print()#10
print()#11
print()#12
print()#13
print()#14
print()#15
print()#16
print()#17
print()#18
print()#19


print(legen)#bottomL

print()

 """

#_____________________________________________________________________________________________________________________

""" CODE BELOW GOES AGAINS AUTOMATION LAWS """

#_____________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________

#Displays  a text message according to the provided bitmap image.

#There are 68 periods along the top and bottom of this string: 
bitmap = """ 
....................................................................
   ***************   *  *** **  *      *****************************
  ********************** ** ** *  * ***************************** * 
**      *******************       *****************************     
         ***************          **  * **** ** ************* *     
          ***********            *******   *************** * *      
           **********           **************************  *       
  *        * ****** ***         *************** ******  ** *        
              ******  *         ***************   *** ***  *        
                ********         *************    **   **  *        
                **********        *************    *  ** ***        
                  **********         ********          * *** ****   
                  ***********         ******  *        **** ** * ** 
                   ***********         ****** * *           *** *  *
                    ********          ***** **             *****   *
                    *******            **** *            ********   
                   *******             ****              *********  
                   ******              **                 *******  *
                   ****                                       *   * 
                   **     *                     *                                
....................................................................
 """ 

print("Enter message to diplay with the bitmap.")
message = input("> ")
if message == "":
    sys.exit()

#Loop over each line in the bitmap:
for line in bitmap.splitlines():
    #Loop over each character in the line:
    for i, bit  in  enumerate(line):
        if bit == " ":
            #Print an empty space since there's a space in the bitmap:
            print(" ", end="")
        else:
            #Print a character from the message:
            print(message[i % len(message)], end="")
    print()