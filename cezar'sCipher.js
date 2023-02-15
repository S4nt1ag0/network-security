
function encrypText(sampleText, key){
    let encryptedText = ''
    for (let i = 0; i < sampleText.length; i++) {
        const letter = sampleText.charAt(i);
        const value = letter.codePointAt(0);
        let keyTemp = key
        if(value >= 65 && value <= 90){
            if( (value + keyTemp) > 90){
                keyTemp -= 26
            }
            encryptedText += String.fromCharCode(value + keyTemp) 
        }else if(value >= 97 && value <= 122){
            if( (value + keyTemp) > 122){
                keyTemp -= 26
            }
            encryptedText += String.fromCharCode(value + keyTemp) 
        }else{
            encryptedText += letter
        }
      }
      return encryptedText
}

let encryptedText = encrypText('Fala Zeze', 5)
console.log(encryptedText)

function decrypText(encryptedText){
    for (let i = 0; i <= 26; i++) {
        let sampleText = ''
        for (let j = 0; j < encryptedText.length; j++) {
            const letter = encryptedText.charAt(j);
            const value = letter.codePointAt(0);
            let key = i
            if(value >= 65 && value <= 90){
                if( (value + key) > 90){
                    key -= 26
                }
                sampleText += String.fromCharCode(value + key) 
            }else if(value >= 97 && value <= 122){
                if( (value + key) > 122){
                    key -= 26
                }
                sampleText += String.fromCharCode(value + key) 
            }else{
                sampleText += letter
            }
          }
        console.log(sampleText)
      }
}

decrypText(encryptedText)
decrypText('cgrzm namfrzmnemzn unem namr fdnm namerzmnmv efdgpnamqrmgzmbdasveeva ny')

