// Binary Agents

// Return an English translated sentence of the passed binary string.
// The binary string will be space separated.


function binaryAgent(str) {
    return str.split(' ').map(bin => String.fromCharCode(parseInt(bin,2))).join('')
  }

function binaryAgent2(binaryString) {
    // Split the binary string into an array of binary numbers
    const binaryArray = binaryString.split(' ');

    // Convert each binary number to its decimal equivalent and map to ASCII characters
    const englishArray = binaryArray.map(binary => String.fromCharCode(parseInt(binary, 2)));

    // Join the characters to form the English sentence
    const englishSentence = englishArray.join('');

    return englishSentence;
}
  
console.log(binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"))


console.log(binaryAgent("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001"))