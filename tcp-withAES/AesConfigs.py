from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)

host = 'localhost'
port = 9098

def encrypt(data, key, iv):
    cipher = Cipher(
    algorithms.AES(key),
    modes.CBC(iv),
    backend=default_backend())
    encryptor = cipher.encryptor()
    return (encryptor.update(data) + encryptor.finalize())

def decrypt(data, key, iv):
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data)
