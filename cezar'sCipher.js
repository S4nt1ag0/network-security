function encrypt(plainText, shift) {
    var encryptedText = "";
  
    for (var i = 0; i < plainText.length; i++) {
      var charCode = plainText.charCodeAt(i);
  
      // Se o caractere estiver em letra maiúscula
      if (charCode >= 65 && charCode <= 90) {
        encryptedText += String.fromCharCode(((charCode - 65 + shift) % 26) + 65);
      }
      // Se o caractere estiver em letra minúscula
      else if (charCode >= 97 && charCode <= 122) {
        encryptedText += String.fromCharCode(((charCode - 97 + shift) % 26) + 97);
      }
      // Se o caracter não for uma letra
      else {
        encryptedText += plainText.charAt(i);
      }
    }
  
    return encryptedText;
  }
  
  function decrypt(encryptedText, shift) {
    var decryptedText = "";
  
    for (var i = 0; i < encryptedText.length; i++) {
      var charCode = encryptedText.charCodeAt(i);
  
      // Se o caractere estiver em letra maiúscula
      if (charCode >= 65 && charCode <= 90) {
        decryptedText += String.fromCharCode(((charCode - 65 - shift + 26) % 26) + 65);
      }
      // Se o caractere estiver em letra minúscula
      else if (charCode >= 97 && charCode <= 122) {
        decryptedText += String.fromCharCode(((charCode - 97 - shift + 26) % 26) + 97);
      }
      // Se o caracter não for uma letra
      else {
        decryptedText += encryptedText.charAt(i);
      }
    }
  
    return decryptedText;
  }
  

let plainText = "teste da cifra de Cezar";
let key = 5;

let encryptedText = encrypt(plainText, key);
console.log(encryptedText);

let decryptedText = decrypt(encryptedText, key);
console.log(decryptedText);