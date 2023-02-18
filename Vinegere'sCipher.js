function encrypt(plainText, key) {
  let encryptedText = "";
  let j = 0;
  let alphabetSize = 26;

  for (let i = 0; i < plainText.length; i++) {
    let charCode = plainText.charCodeAt(i);
    let keyCharCode = key.charCodeAt(j);
    let shift = keyCharCode % alphabetSize;

    if (charCode >= 65 && charCode <= 90) { //Para caracteres maiúsculos 
      encryptedText += String.fromCharCode(((charCode - 65 + shift) % alphabetSize) + 65);
      j = (j + 1) % key.length;
    }
    
    else if (charCode >= 97 && charCode <= 122) { //Para caracteres minúsculos 
      encryptedText += String.fromCharCode(((charCode - 97 + shift) % alphabetSize) + 97);
      j = (j + 1) % key.length;
    }
    // Se não for uma letra 
    else {
      encryptedText += plainText.charAt(i);
    }
  }

  return encryptedText;
}

function decrypt(encryptedText, key) {
  let decryptedText = "";
  let j = 0;
  let alphabetSize = 26;

  for (let i = 0; i < encryptedText.length; i++) {
    let charCode = encryptedText.charCodeAt(i);
    let keyCharCode = key.charCodeAt(j);
    let shift = keyCharCode % alphabetSize;

    if (charCode >= 65 && charCode <= 90) { //Para caracteres maiúsculos
      decryptedText += String.fromCharCode(((charCode - 65 - shift + alphabetSize) % alphabetSize) + 65);
      j = (j + 1) % key.length;
    }
    // If the character is lowercase
    else if (charCode >= 97 && charCode <= 122) { //Para caracteres minúsculos 
      decryptedText += String.fromCharCode(((charCode - 97 - shift + alphabetSize) % alphabetSize) + 97);
      j = (j + 1) % key.length;
    }
    // Se não for uma letra 
    else {
      decryptedText += encryptedText.charAt(i);
    }
  }

  return decryptedText;
  }

let plainText = "teste da cifra de Vinegere";
let key = "wabba dabba dub dub";

let encryptedText = encrypt(plainText, key);
console.log(encryptedText);

let decryptedText = decrypt(encryptedText, key);
console.log(decryptedText);