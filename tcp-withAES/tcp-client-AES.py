import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)
import AesConfigs



s = socket.socket()
host = 'localhost'
port = 9098

def decrypt(data):
    cipher = Cipher(
        algorithms.AES(AesConfigs.key),
        modes.CBC(AesConfigs.iv),
        backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data)


BUFFER_SIZE = 1024

s.connect((host, port))

data = s.recv(BUFFER_SIZE)
print (f"Server response: {data}")
x = decrypt(data).decode()

print(str(x))

s.close()

