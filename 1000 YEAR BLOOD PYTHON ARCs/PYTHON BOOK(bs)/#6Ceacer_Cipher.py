""" The Caesar Cipher is an ancient encryption used by Julius Caesar.
    It encrypts letters by shifting them over by a certain number of places in the alphabet.
    We call the lenght of shift the KEY. 
    For example, if the KEY is 3, then A becomes D, B becomes E, C becomes F, and so on.
    To decrypt the message, you must shift the encrypted letters in the opposite direction.
    This program lets the user encrypt and decrypt messages according to this algorithm. """


print("Caesar Cipher by TYLONs","\n")
ALPHA_U = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

""" def make_AlPHA_L(): #Got lazy yh yh changed my mind so stfu

    for indexA, al in enumerate(ALPHA_U):
        alpha_l.append(al.lower())

    ALPHA_L = tuple(alpha_l)
 """

ALPHA_L = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

encrypt = "E"
#encrypted = ""
decrypt = "D"
#decrypted = ""
meth = "falsy"
key = 0
message = "i love you.  @meriam"
message1 = "A_B_C_D_E"
mes = "NO"
name = "meriam"
name2 = "i love you.  @meriam"
name3 = "i love you. "

def jus_do(): #Gets cipher method n key

    get_Cipher_method()
    print(meth)
    print("You chose {}".format(meth))

    if meth == "E":
        get_key()
        print("The key change is {}".format(key))
        encrypt(key)
    elif meth == "D":
        get_key()
        print("The key change is {}".format(key))
        decrypt(key)
    else:
        print("Error! Check urself nigg")

def get_Cipher_method():#Gets cipher method
    while True: #Ask until it gets corresp response:
        print("Do you want to Encrypt(E) or Decrypt(D)?")
        meth = input("> ")
        meth = meth[0].upper()
        if meth == "E" or meth == "D":          
            break
    print(meth)
    return meth

def get_key():#Gets key
    while True: #Ask until it gets corresp response:
        print("Please enter the key (0 to 26) to use.")
        key = input("> ")
        if key.isdecimal(): #We's looing for an int 0 - 26 
            key = int(key)
            if 0 <= key <= 26:
                break
    return key

def encrypt(key):#Encryption
    print("Enter the message to encrypt.")
    message = input("> ")

    encrypted = ""

    for indexB, let in enumerate(message):
    
        if ALPHA_U.__contains__(let): #If uppercase          
            al_in = ALPHA_U.index(let) #ALPHA_U index 
            change = al_in + key #CIPHERED index
            let = ALPHA_U[change] #CIPHERED letter
        
        elif ALPHA_L.__contains__(let): # If lowercase         
            al_in = ALPHA_L.index(let) #ALPHA_L index
            change = al_in + key #CIPHERED index
            let = ALPHA_L[change] #CIPHERED letter

        encrypted = encrypted.__add__(let) #Add letter to text

    return encrypted

    """ for indexA, letter in enumerate(message):
        print(letter, indexA)
        alpha_index = ALPHA.index(letter.upper()) #Alphabet index
        a = ALPHA.index(letter.upper()) + 1 #Actual alphabet number
        change = alpha_index + key #CIPHERED index
        new_letter = ALPHA[alpha_index] #The new letter
        print("Letter changes to {}  which is alphabet number ({}) and ALPHA index {}".format(new_letter,a,alpha_index))
        print("IF THE KEY IS {} THE LETTER IS CIPHERED TO {}".format(key, ALPHA[change])) """

def decrypt(key):#Decryption
    print("Enter the message to decrypt.")
    message = input("> ")

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

#__________________________________________________________________________________________________________________
""" ONE IN USE """
def cipher():#Cipher method
    while True: #Ask until it gets corresp response:
        print("Do you want to Encrypt(E) or Decrypt(D)?")
        meth = input("> ")
        meth = meth[0].upper()
        if meth == "E" or meth == "D":          
            break
    
    while True: #Ask until it gets corresp response:
        print("Please enter the key (0 to 26) to use.")
        key = input("> ")
        if key.isdecimal(): #We's looing for an int 0 - 26 
            key = int(key)
            if 0 <= key <= 26:
                break

    if meth == "E": #Encrypt
        encrypted_txt = encrypt(key) 
    
        print(encrypted_txt)
        print()
        print("Full encrypted text copied to clipboard.","\n")
    elif meth == "D": #Decrypt
        decrypted_txt = decrypt(key) 

        print(decrypted_txt)
        print()
        print("Full encrypted text copied to clipboard.","\n")
    else:
        print("Nigg YU MAD")
#__________________________________________________________________________________________________________________
 
def run():
    while True:#Loop until they enter QUIT 
        cipher()
        print("Do you wish to Continue? ")
        print("Press any key to continue, or (QUIT) to End Session.")
        cont = input("> ")

        if cont[0].upper() == "Q":#Breakout 
            print("Ending Session.....  Goodbye!")
            break

""" T-T HANDLING METHODS AND STUPID LOCAL VARIABLES IS GIVING ME SIFIA. LORD SIZANI UMTWANA UYA KHALA
print() 
print(meth)
print(key) 
"""
run()

#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________
#
def the_Cipher():

    try:
        import pyperclip # pyperclip copies text to clipboard.
    except ImportError:
        pass #If pyperclip ia not installed, do  nothing. It's no big deal.

    #Every possble symbol that can be encrypted/decrypted:
    """ (!) add numbers and punctuation marks to encrypt? """
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    bshi = """ Caecer cipher encrypts letters by shifting them over by a key number.
            For example, a key of 2 means the letter A is encrypted into C, the letter B encrypted into D, and so on. """

    print(bshi,"\n")

    #let the user enter if the are encrypting or decrypting:
    while True:#keep asking until the user enters E or D.
        print("Do you want to Encrypt(E) or Decrypt(D)?")
        response = input("> ").upper()
        if response.startswith("E"):
            mode = "encrypt"
            break
        elif response.startswith("D"):
            mode = "decrypt"
            break
        print("please enter Encrypt(E) or Decrypt(D).")

    #Let the user enter the key to use:
    while True:#Keep asking until the user enters a valid key.
        maxkey = len(SYMBOLS) - 1
        print("Please enter the key (0 to {}) to use.".format(maxkey))
        response = input("> ")
        if not response.isdecimal():
            continue
        
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

    #Let the user enter the message to encrypt/decrypt:
    print("Enter the message to {}.".format(mode))
    message = input("> ").upper() #Caesar cipher only works on uppercase letters:

    #Stores the encrypted/decrypted form of the message:
    translated = ""

    #Encryp/Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            #Get the encrypted/decrypted number for this symbol.
            num =  SYMBOLS.find(symbol) #get the number of the symbol.
            if mode == "encrypt":
                num += key
            if mode == "decrypt":
                num -= key

            #Handle the wrap-around if num is larger than the length of SYMBOLS or less than 0:
            if num > len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:#Theres a thing wer negative indexes - index from the end of an iterable buh wat evs
                num += len(SYMBOLS)

            #Add encrypted/decrypted number's symbol to translated:
            translated += SYMBOLS[num]
        else:
            #Just add the symbol without encrypting/decrypting:
            translated += symbol

    #Display the encrypted/deccrypted string to the screen:
    print(translated)

    try: 
        pyperclip.copy(translated)
        print("Full {}ed text copied.".format(mode))
    except:
        pass #Do nothing if pyperclip wasn't installed.

def do_The_Cipher():
    while True:#Loop until they enter QUIT 
        the_Cipher()
        print("Do you wish to Continue? ")
        print("Press any key to continue, or (QUIT) to End Session.")
        cont = input("> ")

        if cont[0].upper() == "Q":#Breakout 
            print("Ending Session.....  Goodbye!")
            break

do_The_Cipher()
#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________