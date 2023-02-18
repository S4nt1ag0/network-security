import numpy as np
from egcd import egcd

alphabet = np.array(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z', ' '])

toInt = lambda char: np.where(alphabet == char.upper())[0][0]
toChar = lambda int: alphabet[int]


def getInverse(key):
    inverseKey = np.linalg.inv(key)
    det = int(np.round(np.linalg.det(key)))
    det_inv = egcd(det, 27)[1] % 27
    result = (det_inv * np.round(det * inverseKey).astype(int) % 27)
    return result


def encrypt(plainText, key):
    chars = list(plainText)
    arrayOfIndex = np.array(list(map(toInt, chars)))
    encryptText = ""
    while len(arrayOfIndex) > 0:
        pairArray = arrayOfIndex[:2]
        arrayOfIndex = arrayOfIndex[2:]
        hasProblem = False
        if (len(pairArray) < 2):
            hasProblem = True
            pairArray = np.append(pairArray, 0)
        c = np.matmul(pairArray, key)
        if (hasProblem):
            c = np.delete(c, [1])
        c = np.mod(c, 27)
        c = np.array(list(map(toChar, c)))
        encryptText = encryptText + "".join(str(char) for char in c)
    return encryptText


def decrypt(encryptText, key):
    inverseKey = getInverse(key)
    chars = list(encryptText)
    arrayOfIndex = np.array(list(map(toInt, chars)))
    plainText = ""
    size = len(inverseKey)
    while len(arrayOfIndex) > 0:
        pairArray = arrayOfIndex[:size]
        arrayOfIndex = arrayOfIndex[size:]
        hasProblem = False
        if (len(pairArray) < size):
            hasProblem = True
            pairArray = np.append(pairArray, 0)
        p = np.matmul(pairArray, inverseKey)
        p = np.mod(p, 27)
        if (hasProblem):
            p = np.delete(p, [1])
        p = np.array(list(map(toChar, p)))
        plainText = plainText + "".join(str(char) for char in p)
    return plainText


key = np.array([[9, 4], [5, 7]])

message = "teste da cifra de hill dois x dois"
print("Mensagem Original:")
print(message)

encryptText = encrypt(message, key)
print("Mensagem Encriptada:")
print(encryptText)

plainText = decrypt(encryptText, key)
print("Mensagem Decriptada")
print(plainText)