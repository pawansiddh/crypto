import socket
import datetime
import random

s = socket.socket()

# Assuming 'a' is a predefined list
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(random):
    key += random.choice(a)


def toLowerCase(text):
    return text.lower()


def removeSpaces(text):
    newText = ""
    for i in text:
        if i != ' ':
            newText += i
    return newText


def Diagraph(text):
    Diagraph = []
    for i in range(0, len(text), 2):
        Diagraph.append(text[i:i+2])
    return Diagraph


def FillerLetter(text, k):
    newText = ""
    for i in range(0, k, 2):
        if text[i] == text[i + 1]:
            new_word = text[i:i + 2] + str(random.choice(a))
            new_word = FillerLetter(new_word, len(new_word))
            break
        else:
            new_word = text[i:i + 2]
    else:
        new_word = text
    return new_word


def generateKeyTable(word, text):
    new_word_list = []

    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    complement = []
    for i in key_letters:
        if i not in complement:
            complement.append(i)

    for i in text:
        if i not in complement:
            complement.append(i)

    matrix = [complement[i:i + 5] for i in range(0, len(complement), 5)]
    complement = complement[5:]

    return matrix


def search(mat, element):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:
                return i, j


def encrypt_RowRule(matr, elr, elc, e2r, e2c):
    char1 = matr[elr][elc + 1] if elc != 4 else matr[elr][0]
    char2 = matr[e2r][e2c + 1] if e2c != 4 else matr[e2r][0]
    return char1, char2


def encrypt_ColumnRule(matr, elr, elc, e2r, e2c):
    char1 = matr[elr + 1][elc] if elr != 4 else matr[0][elc]
    char2 = matr[e2r + 1][e2c] if e2r != 4 else matr[0][e2c]
    return char1, char2


def encrypt_RectangleRule(matr, elr, elc, e2r, e2c):
    char1 = matr[elr][e2c]
    char2 = matr[e2r][elc]
    return char1, char2


def encryptByPlayfairCipher(matrix, plainList):
    CipherText = []
    for i in range(len(plainList)):
        ele1_x, ele1_y = search(matrix, plainList[i][0])
        ele2_x, ele2_y = search(matrix, plainList[i][1])

        if ele1_x == ele2_x:
            char1, char2 = encrypt_RowRule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            char1, char2 = encrypt_ColumnRule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            char1, char2 = encrypt_RectangleRule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = char1 + char2
        CipherText.append(cipher)

    return CipherText


textPlain = "hello"
PlainTextList = Diagraph(removeSpaces(toLowerCase(textPlain)))
key = toLowerCase("your_key_here")  # Replace with your key

key = removeSpaces(key)
Matrix = generateKeyTable(key, a)
CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
    CipherText += i

print("Key:", key)
print("CipherText:", CipherText)

s.listen(5)
print("Server is up and running")

while True:
    c, addr = s.accept()
    print("Connected to", addr)
    c.send(key.encode())
    msg1 = c.recv(1024).decode()
    print(msg1)
    msg = msg1.split(',')
    print()
    if msg:
        print("Accepted")
    else:
        print("Rejected")

s.close()
