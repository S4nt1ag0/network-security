import socket
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)
import AesConfigs

def encrypt(data):
    cipher = Cipher(
    algorithms.AES(AesConfigs.key),
    modes.CBC(AesConfigs.iv),
    backend=default_backend())
    encryptor = cipher.encryptor()
    return (encryptor.update(data) + encryptor.finalize())

HOST = sys.argv[1]             #host
PORT = int(sys.argv[2])        #port
plaintext = sys.argv[3]        #message

while len(plaintext)%16 != 0:
    plaintext += " "

plaintext = plaintext.encode()
x = encrypt(plaintext)

# definições do socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('\nsocket bind to port: %s' % (PORT))

# aguardando requisições
s.listen()
print("socket is listening")

try:
    while True:
        # aceitando conexão com o client
        clientSocket, addr = s.accept()
        print('[port: %s] new connection with client' % (addr[1]))
        clientSocket.send(x)
except:
    pass
finally:
    print("SERVER OFF %s:%s" % (HOST, PORT))
    s.close()