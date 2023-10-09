import random

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mod_inverso(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def geraParChaves(keysize = 16):
    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    primos = [2]
    ini = 1 << (keysize // 2 - 1)
    fim = 1 << (keysize // 2 + 1)

    for i in range(3, fim + 1, 2):
        isPrime = True
        for p in primos:
            if i % p == 0:
                isPrime = False
                break
        if(isPrime):
            primos.append(i)

    while (primos and primos[0] < ini):
        del primos[0]
    while primos:
        p = random.choice(primos)
        primos.remove(p)
        q_values = [q for q in primos if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break

    print(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(1, phi)
        g = mdc(e, phi)
        # gera chave privada
        d = mod_inverso(e, phi)
        if g == 1 and e != d:
            break
    # chave pública (e,n)
    # chave privada (d,n)
    return ((e, n), (d, n))

def criptografa(msg_original, chave_valor):
    e, n = chave_valor
    msg_cifrada = [pow(ord(c), e, n) for c in msg_original]
    return msg_cifrada

def descriptografa(msg_cifrada, chave_valor):
    d, n = chave_valor
    msg_original = [chr(pow(c, d, n)) for c in msg_cifrada]
    return (''.join(msg_original))

# -------------------------------------------------------------
print("Iniciando algoritmo RSA...")
print("Gerando par de chaves privadas/públicas...")
publica, privada = geraParChaves(16)
print("Chave pública:", publica)
print("Chave privada:", privada)
msg = input("Mensagem que deseja criptografar:")
msg_criptografada = criptografa(msg, publica)
print("Mensagem criptografada:")
print(''.join(map(lambda x: str(x), msg_criptografada)))
print("Mensagem descriptografada:")
print(descriptografa(msg_criptografada, privada))