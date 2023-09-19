ALPHA = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
alc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
encrypt = "E"
decrypt = "D"
meth = ""
key = 1
message = "A_B_C_D_E"
mes = "NO"
name = "meriam"
name2 = "i love you.  @meriam"
name3 = "i love you. "

mes = message.replace("A","b")

print(name.upper())

""" for indexA, letter in enumerate(name):
    print(letter, indexA)
    alpha_index = ALPHA.index(letter.upper()) #Alpha index
    a = ALPHA.index(letter.upper()) + 1 #Actual alphabet number
    change = alpha_index + key #CIPHERED index
    new_letter = ALPHA[alpha_index] #The new letter
    print("Letter changes to {}  which is alphabet number ({}) and ALPHA index {}".format(new_letter,a,alpha_index))
    print("IF THE KEY IS {} THE LETTER IS CIPHERED TO {}".format(key, ALPHA[change])) """

encrypted = ""
decrypted = ""

for indexB, let in enumerate(name2):
    
    if ALPHA.__contains__(let.upper()):
        
        al_in = ALPHA.index(let.upper()) #Alpha index
        change = al_in + key #CIPHERED index
        let = ALPHA[change]
    encrypted = encrypted.__add__(let)
    print(encrypted)

for indexB, let in enumerate(encrypted):
    
    if ALPHA.__contains__(let.upper()):
        
        al_in = ALPHA.index(let.upper()) #Alpha index
        change = al_in - key #CIPHERED index
        let = ALPHA[change]
    decrypted = decrypted.__add__(let)
    print(decrypted)   


def encrypt(key):#Encryption
    print("Enter the message to encrypt.")
    message = input("> ")

    for indexB, let in enumerate(message):
    
        if ALPHA.__contains__(let.upper()):
            
            al_in = ALPHA.index(let.upper()) #Alpha index
            change = al_in + key #CIPHERED index
            let = ALPHA[change]
        encrypted = encrypted.__add__(let)
    return encrypted

def decrypt(key):#Decryption
    print("Enter the message to decrypt.")
    message = input("> ")

    for indexB, let in enumerate(message):
    
        if ALPHA.__contains__(let.upper()):
            
            al_in = ALPHA.index(let.upper()) #Alpha index
            change = al_in + key #CIPHERED index
            let = ALPHA[change]
        decrypted = decrypted.__add__(let)
    return decrypted


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
    
    encrypted = ""
    decrypted = ""

    if meth == "E":
        print("Enter the message to encrypt.")
        message = input("> ")

        for indexB, let in enumerate(message):
    
            if ALPHA.__contains__(let.upper()):
            
                al_in = ALPHA.index(let.upper()) #Alpha index
                change = al_in + key #CIPHERED index
                let = ALPHA[change]
            encrypted = encrypted.__add__(let)
        print(encrypted)
        print()
        print("Full encrypted text copied to clipboard.","\n")
    elif meth == "D": 
        print("Enter the message to decrypt.")
        message = input("> ")

        for indexB, let in enumerate(message):
        
            if ALPHA.__contains__(let.upper()):
                
                al_in = ALPHA.index(let.upper()) #Alpha index
                change = al_in + key #CIPHERED index
                let = ALPHA[change]
            decrypted = decrypted.__add__(let)
        print(decrypted)
        print()
        print("Full encrypted text copied to clipboard.","\n")
    else:
        print("Nigg YU MAD")

    

""" print(name2)
print()
print(encrypted)
print(decrypted) """
print("TYLONs")

print()
print()
cipher()