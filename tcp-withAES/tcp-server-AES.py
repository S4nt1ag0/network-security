import socket
import AesConfigs
import rsa

#chave publica, privada
publicKey, privateKey = rsa.newkeys(2048)
BUFFER_SIZE = 1024
# definições do socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((AesConfigs.host, AesConfigs.port))
print('\nsocket bind to port: %s' % (AesConfigs.port))

s.listen()
print("socket is listening")

try:
    while True:
        # aceitando conexão com o client
        clientSocket, addr = s.accept()
        print('[port: %s] new connection with client' % (AesConfigs.port))
        clientSocket.send(publicKey.save_pkcs1())
        keyForAes = clientSocket.recv(BUFFER_SIZE)
        keyForAes = rsa.decrypt(keyForAes,privateKey)
        ivForAes = clientSocket.recv(BUFFER_SIZE)
        print(ivForAes)
        ivForAes = rsa.decrypt(ivForAes,privateKey)
        print(ivForAes)
        encryptedText = clientSocket.recv(BUFFER_SIZE)
        decryptedText = AesConfigs.decrypt(encryptedText, keyForAes, ivForAes).decode()
        clientSocket.send('Tudo certo, texto descriptogrfado: '+ decryptedText).encode('utf-8')
        clientSocket.close()
except:
    pass
finally:
    print("SERVER OFF %s:%s" % (AesConfigs.host, AesConfigs.port))
    s.close()







# aguardando requisições


