def decrypt(key):#Decryption
    print("Enter the message to decrypt.")
    message = input("> ")

    for indexB, let in enumerate(message):
    
        if ALPHA.__contains__(let.upper()):
            
            al_in = ALPHA.index(let.upper()) #Alpha index 
            change = al_in - key #CIPHERED index
            let = ALPHA[change]
        decrypted = decrypted.__add__(let)
    return decrypted


KPCFEJ  = "tylons"
