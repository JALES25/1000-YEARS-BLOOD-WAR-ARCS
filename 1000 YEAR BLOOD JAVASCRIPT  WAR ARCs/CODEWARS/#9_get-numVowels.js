//DAY 3



/** #2
 * Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    The input string will only consist of lower case letters and/or spaces.
 */


const numVowels = str =>  ((str || '').match(/[aeiou]/ig)||[]).length

/** #2 <6-kata>
 * 
 */
const isPangram =  str =>  {
    const  alph = new Set('abcdefghijklmnopqrstuvwxyz');
     str =  str.toLowerCase();
    
    for (let letter of  str) {
         alph.delete(letter);
    }
    
    return  alph.size === 0;
}


/**
 * 
 */

const getSum = (a, b) => {
    sum = 0
   const temp = [a,b]
   temp.sort((a,b) => a - b)
   for (let i = temp[0]; i < temp[1]; i++) {
     sum+= i
   }
   return sum
 }

 console.log(getSum(5,-1))