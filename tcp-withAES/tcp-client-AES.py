import socket

import rsa

import AesConfigs

keyForAES = b'key must be 128.'
ivForAES = b"\x8a'\xd8\xf59]\x157S[X\xc0t\xcb\xa2\xc8"
BUFFER_SIZE = 1024

plaintext = input("Message a ser criptografada: ")

while len(plaintext)%16 != 0:
    plaintext += " "
plaintext = plaintext.encode()
encryptedText = AesConfigs.encrypt(plaintext, keyForAES, ivForAES)


s = socket.socket()


s.connect((AesConfigs.host, AesConfigs.port))
serverPublicKey = s.recv(BUFFER_SIZE)
serverPublicKey = rsa.PublicKey.load_pkcs1(serverPublicKey)
encryptedKeyForAES = rsa.encrypt(keyForAES, serverPublicKey)
s.send(encryptedKeyForAES)
encryptedIvForAES = rsa.encrypt(ivForAES, serverPublicKey)
s.send(encryptedIvForAES)
s.send(encryptedText)



serverReturn = s.recv(BUFFER_SIZE).decode('utf-8')
print (f"Server response: {serverReturn}")

s.close()

