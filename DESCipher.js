const initial_message_permutation =	   [58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6,
           64, 56, 48, 40, 32, 24, 16, 8,
           57, 49, 41, 33, 25, 17,  9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7];

const tableS = [
    [
        [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
        [0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
        [4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
        [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
    ],
    [
        [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
        [3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
        [0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
        [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]
    ],
    [
        [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
        [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
        [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
        [1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]
    ],
    [
        [7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
        [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
        [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
        [3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]
    ],
    [
        [2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
        [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
        [4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
        [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]
    ],
    [
        [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
        [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
        [9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
        [4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]
    ],
    [
        [4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
        [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
        [1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
        [6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]
    ],
    [
        [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
        [1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
        [7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
        [2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]
    ]
]
const sub_message_permutation =    [
    16,  7, 20, 21,
       29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]

function functionF(Re){
    let newRe = []
    for(j = 0; j<48; j++){ //expansão de Re de 32 bits para 48 bits acrescentando 0
        newRe[j] = parseInt(Re[j])
        if(j>31){
            newRe[j] = 0
        }
    }

    for(j = 0; j<48; j++){ //XOR entre newRe e as chaves, como a chave é uma sequência de 1, sempre será 1, que simplica a operação xor
        if(newRe[j]){
            newRe[j] = 0
        }else{
            newRe[j] = 1
        }
    }
    //iniciando a substituição de caixa-S
    let beforeS = [];
    beforeS[0] = newRe.splice(0,6)
    beforeS[1] = newRe.splice(0,6)
    beforeS[2] = newRe.splice(0,6)
    beforeS[3] = newRe.splice(0,6)
    beforeS[4] = newRe.splice(0,6)
    beforeS[5] = newRe.splice(0,6)
    beforeS[6] = newRe.splice(0,6)
    beforeS[7] = newRe.splice(0,6)

    let afterS = ''
    for(j = 0; j<8; j++){
        let row = ''+beforeS[j][0]+''+beforeS[j][5]+''
        let col = ''+beforeS[j][1]+''+beforeS[j][2]+''+beforeS[j][3]+''+beforeS[j][4]+''
        row = parseInt(row,2)
        col = parseInt(col,2)
        let value = tableS[j][row][col]
        value = value.toString(2)
        for(k = value.length; k <4; k++){
            value = '0'+value
        }
        afterS = afterS + value
    }

    //Permutação do produto da substituição da caixa-S
    let newRePermuted = []
    for(j = 0; j<32;j++){
        let newIndexPermuted = sub_message_permutation[j]
        newRePermuted[j] = afterS[newIndexPermuted - 1]
    }
    
    return newRePermuted
}

function encrypt(plainText, roundCount) {
let plaintTextTemp = plainText

for(i = plainText.length; i <= 64; i++){
    plaintTextTemp = '0'+plaintTextTemp
}

let permutedText = []

for(i=0; i<64; i++){
    let permutedIndex = initial_message_permutation[i]
    permutedText[i]= plaintTextTemp[permutedIndex - 1]
}
let cipherText = []
cipherText[0] = permutedText
for(round = 1; round<=roundCount; round++){
    cipherText[round] = [];
    for(i=32; i<64; i++){
        cipherText[round][i-32] = cipherText[round - 1][i-32]
    }

    ReTemp = cipherText[round - 1].slice(0, 32)
    LeTemp = cipherText[round - 1].slice(32, 64)
    const Re = functionF(ReTemp)

    let newRe = []
    for(j = 0; j<32;j++){ //XOR entre o Re gerado pela função F e o Re
        if(parseInt(Re[j]) == parseInt(LeTemp[j])){
            newRe[j] = ''+0+''
        }else{
            newRe[j] = ''+1+''
        }
    }
    for(i=0; i<32; i++){
        cipherText[round][i+32] = newRe[i]
    }
}

return cipherText.slice(-1)
}

const binRandom = '111101000010101001010000100000100'

encryptedText = encrypt(binRandom, 2)[0]
console.log('Os Bits na posição 1, 16, 33 e 48 são: ')
console.log(encryptedText[0], encryptedText[15], encryptedText[32], encryptedText[48])