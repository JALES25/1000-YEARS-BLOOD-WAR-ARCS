// DNA Pairing

// Pairs of DNA strands consist of nucleobase pairs. 
// Base pairs are represented by the characters AT and CG, which form building blocks of the DNA double helix.

// The DNA strand is missing the pairing element. 
// Write a function to match the missing base pairs for the provided DNA strand. 
// For each character in the provided string, find the base pair character. 
// Return the results as a 2d array.

// For example, for the input GCG, return [["G", "C"], ["C","G"], ["G", "C"]]

// The character and its pair are paired up in an array, 
// and all the arrays are grouped into one encapsulating array.

//INSTRUCTIONS UNCLEAR???? ENDED UP JUST PAIRING EACH LETTER WITH ITS CORREPONDING DNA LETTER

function pairElement(str) {
    return Array.from(str).map(dna => 
        (dna == "A")? [dna,"T"] :
        (dna == "T")? [dna, "A"] :
        (dna == "C")? [dna, "G"] :
        (dna == "G")? [dna, "C"] : null
      )
  }

const pairElement2 = str => {
  const dnaPairs = {
    A: ["A", "T"],
    T: ["T", "A"],
    C: ["C", "G"],
    G: ["G", "C"]
  };

  return str.split('').map(dna => dnaPairs[dna] || null);
}
  
  console.log(pairElement("GCG"))
  console.log(pairElement("ATCGA"))
  console.log(pairElement("TTGAG"))
  console.log(pairElement2("CTCTA"))