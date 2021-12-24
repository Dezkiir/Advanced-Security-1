import string

plain_text = input("Enter Message to be Encrypted: ")
print("Key Must be Integer")
shift = int(input("Enter Key: "))
shift %=26
alphabet = string.ascii_letters

#Shiftinhg the Alphabet by the Key
shifted_alphabet= alphabet[shift:] + alphabet[:shift]
#Mapping the Alphabet to the new Shifted Alphabet
eTable = str.maketrans(alphabet, shifted_alphabet)
#Mapping the Shifted Alphabet to the Alphabet
dTable = str.maketrans(shifted_alphabet, alphabet)
#Translating the Plain Text String into the new Encrypted String
encrypted = plain_text.translate(eTable)
#Translating the Encrypted String back into the Plain Text String
decrypted = encrypted.translate(dTable)
print(encrypted)
print(decrypted)