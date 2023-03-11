import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)
import AesConfigs



s = socket.socket()
host = 'localhost'
port = 9098

print(AesConfigs.iv)
def decrypt(data):
    cipher = Cipher(
        algorithms.AES(AesConfigs.key),
        modes.CBC(AesConfigs.iv),
        backend=default_backend())
    decryptor = cipher.decryptor()
    print((decryptor.update(data))[16:])


BUFFER_SIZE = 1024

s.connect((host, port))

data = s.recv(BUFFER_SIZE)
print(data)
x = decrypt(data)

