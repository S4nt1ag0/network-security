from string import ascii_lowercase, punctuation, digits, ascii_uppercase
caracters = [ascii_lowercase, punctuation, digits, ascii_uppercase]
caracters = ''.join(caracters)

def insertSeed():
    while True:
        seed = input('Informe a seed para gerar a senha, ou 0 para usar a seed default')
        seed = int(seed)
        if(seed == 0):
            seed = 638206156841347639269316360683780624669997824899092613657499996299360748240205270634473231376134238523703498937006738975966712153078460409342717174837564978234246272432170801528660384587121258596198410392172163957296330019165104690057337051452119292662879930926326479961905925372244001788254297307067692618886724682914363964985937853211919285395505739985348810758435277310902675078566987081097647747346050466355754516394643962446924343203528091100141666739604315166651396941144832198609834115568102217138336008341988543359125439727729547470385088424294130098323933882116391585970155415584959
        return seed

def bbs_random_number(seed, n):
    x = seed
    result = []
    m = 518987503  #multiplicação de dois numeros primos grandes 7919 * 65537

    for i in range(n):
        x = pow(x, 2, m)
        result.append(int(x))

    return result

def gen_password(bbs):
    password = ''
    for number in bbs:
        password += caracters[number % len(caracters)]
    return password


seed = insertSeed()
bbs = bbs_random_number(seed,16)
password = gen_password(bbs)

print(password)

