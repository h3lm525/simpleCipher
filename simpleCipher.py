#python 3
import pyperclip

cipher = 'abcdefghijklmnopqrstuvwxyz'  #all letters for encryption
cipherNums = '0123456789'              #all numbers for encryption
cipherSymbols = '=+-;:{}[]!?@#$%^&*().,\'"/' #all symbols for encryptions


def Decide(Encrypt, Decrypt):
    
    while True: #select encrypt/decrypt/both and error trap selection
        print('Hello! Would you like to Encrypt, Decrypt, or Both?')
        selection = input('*Only PlainText Encrypted with this specific Algorithm with Decrypt Successfully*\n').lower()
        if selection =='encrypt':
            Encrypt(cipher, cipherNums, cipherSymbols)
            break
        elif selection =='decrypt':
            encryptedMessage = input('Enter Encrypted Message\n')
            Decrypt(cipher, cipherNums, cipherSymbols, encryptedMessage)
            break
        elif selection =='both':
            encryptedCipherText = Encrypt(cipher, cipherNums, cipherSymbols)
            print('\n')
            Decrypt(cipher, cipherNums, cipherSymbols, encryptedCipherText)
            break
        else:
            print('Invalid Selection. Please try again.\n')
            continue
        

def Encrypt(cipher, cipherNums, cipherSymbols):
    plainText = input("Enter Plain-Text: ").lower()
    count = 0; #used for comparison between plaintext and alphabet
    encrypted = []
    finalEncrypted = '' #placeholder for message to be copied to clipboard
    for i in plainText:
        for j in cipher:
            if i.isspace(): #keep spaces intact inside encryption
                encrypted.append(i)
                break
            elif i in cipherSymbols: #not encrypting symbols for clarity
                encrypted.append(i)
                break
            elif i in cipherNums:
                encrypted.append(i)
                break
            elif i == j: #encrypt by shifting 3 places
                if count in range(24, 26): #used to encrypt x, y and z
                    count -= 26
                    encrypted.append(cipher[count + 3])
                    break
                else:   #used for all other letters
                    encrypted.append(cipher[count + 3])
                    break
            
            else:
                count += 1
        count = 0
    print("Original PlainText: ", plainText)
    finalEncrypted = ''.join(str(i) for i in encrypted)
    finalEncrypted = finalEncrypted[::-1]
    print("Encrypted Message: ", finalEncrypted)
    print("Encrypted Message copied to Clipboard!")
    pyperclip.copy(finalEncrypted)#copy encrypted message to clipboard
    return finalEncrypted

def Decrypt(cipher, cipherNums, cipherSymbols, cipherText):
    #works the same as Encrypt() in reverse
    count = 0
    decrypted = []
    finalDecrypted = ''
    
    for i in cipherText:
        for j in cipher:
            if i.isspace():
                decrypted.append(i)
                break
            elif i in cipherSymbols:
                decrypted.append(i)
                break
            elif i in cipherNums:
                decrypted.append(i)
                break
            elif i == j:
                decrypted.append(cipher[count -3])
                break
            else:
                count += 1
        count = 0
    print("Original CipherText: ", cipherText)
    finalDecrypted = ''.join(str(i) for i in decrypted)
    finalDecrypted = finalDecrypted[::-1]
    print("Decrypted Message: ", finalDecrypted)
    return finalDecrypted

Decide(Encrypt, Decrypt)                       


                                     







