import random

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def generateKeyPair(keysize = 16):
    #configurando tamanho da chave, valores maximos, minimos e de onde começa e termina a geração.
    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    primos = [2]
    start = 1 << (keysize // 2 - 1)
    end = 1 << (keysize // 2 + 1)

    #Selecionando todos os primos entre start e end.
    for i in range(3, end + 1, 2):
        isPrime = True
        for p in primos:
            if i % p == 0:
                isPrime = False
                break
        if(isPrime):
            primos.append(i)

    #Excluindo os primos menores que o valor inicial
    while (primos and primos[0] < start):
        del primos[0]

    #Dos primos restantes, seleciona um aleatorio para ser p, e outro para ser q, desde que p*q não seja maior que nMax
    while primos:
        p = random.choice(primos)
        primos.remove(p)
        q_values = [q for q in primos if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break

    print("p e q:", p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    #gera a chave publica e privada desde que mdc(e, phi) == 1 e 'e' != d
    while True:
        e = random.randrange(1, phi)
        g = mdc(e, phi)
        # gera chave privada
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break
    # chave pública (e,n)
    # chave privada (d,n)
    return ((e, n), (d, n))

def criptografa(msg_original, chave_valor):
    e, n = chave_valor
    #para cada caractere da mensagem original, seu valor na tabela ascii é elavado a 'e' e calculado o mod n
    msg_cifrada = [pow(ord(c), e, n) for c in msg_original]
    return msg_cifrada

def descriptografa(msg_cifrada, chave_valor):
    d, n = chave_valor
    #Cada número da mensagem criptografada é elavado a d e calculado o mod n, então se extrai o caractere correspondente
    #a esse valor na tabela ascii
    msg_original = [chr(pow(c, d, n)) for c in msg_cifrada]
    return (''.join(msg_original))

# -------------------------------------------------------------
print("Iniciando algoritmo RSA...")
print("Gerando par de chaves privadas/públicas...")
publica, privada = generateKeyPair()
print("Chave pública:", publica)
print("Chave privada:", privada)
msg = input("Mensagem que deseja criptografar:")
msg_criptografada = criptografa(msg, publica)
print("Mensagem criptografada:")
print(''.join(map(lambda x: str(x), msg_criptografada)))
print("Mensagem descriptografada:")
print(descriptografa(msg_criptografada, privada))