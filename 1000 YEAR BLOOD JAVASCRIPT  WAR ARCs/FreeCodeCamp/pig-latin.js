// Pig Latin

// Pig Latin is a way of altering English Words. The rules are as follows:
// - If a word begins with a consonant, take the first consonant or consonant cluster, 
// move it to the end of the word, and add ay to it.
// - If a word begins with a vowel, just add way at the end.

import { diffArray } from "./Diff-two-arrays";
  
  function translatePigLatin(str) {
    const consosMatch = str.match(/[^aeiou]+(?=[aeiou])/ig);
    const consos = consosMatch ? consosMatch[0].split('') : [];
    
    if (consos.length === 0) {
      // Handle the case where there are no consonants before the first vowel
      return str + 'way';
    }
  
    // Use the diffArray function to translate to Pig Latin
    const translated = diffArray(consos, str);
    return translated.join('') + 'ay';
  }

  function pigLatin(str) {
  // Function to check if a character is a vowel
  const isVowel = (char) => 'aeiouAEIOU'.includes(char);

  // Check if the first character is a consonant or a vowel
  if (isVowel(str[0])) {
    // If it's a vowel, just add "way" at the end
    return str + 'way';
  } else {
    // If it starts with a consonant, find the first vowel
    let firstVowelIndex = 0;
    while (firstVowelIndex < str.length && !isVowel(str[firstVowelIndex])) {
      firstVowelIndex++;
    }

    // Move the consonant cluster to the end and add "ay"
    const consonantCluster = str.slice(0, firstVowelIndex);
    const restOfWord = str.slice(firstVowelIndex);
    return restOfWord + consonantCluster + 'ay';
  }
}




  