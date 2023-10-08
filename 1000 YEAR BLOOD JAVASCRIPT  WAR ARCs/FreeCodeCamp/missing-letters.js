    // Missing letters

    // Find the missing letter in the passed letter range and return it.

    // If all letters are present in the range, return undefined.


function fearNotLetter(str) {
  for (let i = 0; i < str.length - 1; i++) {
    const currentCharCode = str.charCodeAt(i);
    const nextCharCode = str.charCodeAt(i + 1);

    if (nextCharCode - currentCharCode > 1) {
      return String.fromCharCode(currentCharCode + 1);
    }
  }

  return undefined;
}


function fearNotLetters(str) {
  const alphs = "abcdefghijklmnopqrstuvwxyz"
  let tempS = str.split('').sort()
  const maxL = tempS[tempS.length-1]
  const minL = tempS[0]
  const tempAl = alphs.slice(minL, alphs.indexOf(maxL) + 1)
  const missingL = []
  tempAl.split('').forEach(letter => !tempS.includes(letter)? missingL.push(letter) : null)

 
  return (missingL.length == 0)? undefined : missingL
}

console.log(fearNotLetter("abce"))
console.log(fearNotLetter("abcdefghjklmno"))
console.log(fearNotLetter("stvwx"))
console.log(fearNotLetter("bcdf"))
console.log(fearNotLetter("abcdefghijklmnopqrstuvwxyz"))
