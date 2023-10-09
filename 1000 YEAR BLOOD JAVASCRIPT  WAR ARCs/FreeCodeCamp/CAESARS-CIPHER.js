// Caesars Cipher

// One of the simplest and most widely known ciphers is a Caesar cipher, 
// also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.

// A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. 
// Thus A ↔ N, B ↔ O and so on.

// Write a function which takes a ROT13 encoded string as input and returns a decoded string.

// All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), 
// but do pass them on.



function rot13(str) {
  const ALPHs = []
  

  function generateAlphabet() {
    
    for (let i = 65; i <= 90; i++) {
      ALPHs.push(String.fromCharCode(i))
    }
    return ALPHs
  }
  generateAlphabet()
  
  const ALPHx2 = ALPHs.concat(ALPHs)
  const decArr = []
  for (let char of str) {
    (ALPHs.includes(char))? 
      decArr.push(ALPHx2[ALPHx2.indexOf(char) + 13]) :
      decArr.push(char)
  }

  return decArr.join('') 
}

console.log(rot13("SERR PBQR PNZC"))
console.log(rot13("SERR YBIR?"))