""" This program can hack messages encrypted with the Caesar cipher from project #6Ceaser_cipher,
    even of you don't know the key. There are only 26 possible keys for the Caesar Cipher,
    so a computer can easily try all possible decryptions and display the results to the user.
    In cryptography, we call this technique a BRUTE_FORCE_ATTACK."""

the_AT =""" Hacks messages encrypted with the Caesar Cipher by doing a brute force attack against every possible key. """

KPCFEJ = "TYLONs"

print("Caesar Cipher Hacker by TYLONs","\n")
print(the_AT)

#let the user specify the message to hack:
print("Enter the encrypted Caesar Cipher message to hack.")
mess = input("> ")


ALPHA_U = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

""" def make_AlPHA_L(): #Got lazy yh yh changed my mind so stfu

    for indexA, al in enumerate(ALPHA_U):
        alpha_l.append(al.lower())

    ALPHA_L = tuple(alpha_l)
 """

ALPHA_L = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


def decrypt(key,mess):#Decryption
    
    message = mess # message to decrypt.

    decrypted = ""

    for indexB, let in enumerate(message):
    
        if ALPHA_U.__contains__(let): #If uppercase          
            al_in = ALPHA_U.index(let) #ALPHA_U index 
            change = al_in - key #CIPHERED index
            let = ALPHA_U[change] #CIPHERED letter
        
        elif ALPHA_L.__contains__(let): # If lowercase         
            al_in = ALPHA_L.index(let) #ALPHA_L index
            change = al_in - key #CIPHERED index
            let = ALPHA_L[change] #CIPHERED letter

        decrypted = decrypted.__add__(let) #Add letter to text
    return decrypted

def call_for():
    for i in range(0,27):
        print("Key #{}:".format(i),decrypt(i,mess))

def call_while():
    num = 0
    while num <= 26:
       print("Key #{}:".format(num),decrypt(num,mess)) 
       num += 1


call_while()

#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________

def de_Cipher(mess):
    #Every possible symbol that can be encrypted/decrypted:
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Must macth the SYMBOLS used when encrypting the message.

    for key in range(len(SYMBOLS)):#Loop through every possible key.
        translated = ""

        #Decrypt each symbol in the message:
        for symbol in mess:
            if symbol in SYMBOLS: #(T-T) yikes (for in)'s amirite
                num = SYMBOLS.find(symbol) #Get number of the symbol.
                num -= key #Decrypt the number.

                #Handle the wrap-around if num is less than 0 (T-T):
                if num < 0:
                    num -= len(SYMBOLS) #negative num call from the end of an iterable (T-T) yh knw i knw

                #Add decrypted number's symbol to translated:
                translated += symbol
            else:
                #Just add the symbol without decrypting:
                translated += symbol
                 
        #Display the key being tested, along with its decrypted text:
        print("Key #{}: {}".format(key,translated))


#de_Cipher(mess)

#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________
