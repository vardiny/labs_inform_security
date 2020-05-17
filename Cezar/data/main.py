import keyFile


def encryption(encrypt):
    encrypt = encrypt.lower()
    characters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in encrypt:
        notEncrypted = characters.find(letter)
        encryptCharacters = notEncrypted + keyFile.key
        if letter in characters:
            encrypted = encrypted + characters[encryptCharacters]
        else:
            encrypted = encrypted + letter
    return encrypted


readFile = open('../data/encrypt.txt', 'r')
text = "".join(readFile)
gg = encryption(text)
writeFile = open('../data/encrypted.txt', 'w')
writeFile.writelines(gg)
writeFile.close()
