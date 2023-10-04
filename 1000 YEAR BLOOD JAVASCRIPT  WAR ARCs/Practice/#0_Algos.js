/** #1
 * Convert Celsius to Fahrenheit
    The formula to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.
 */
const convertCtoF = celsius => (celsius * 9/5) + 32
  
convertCtoF(30)

/** #2
 * Reverse a String
    Reverse the provided string and return the reversed string.
    For example, "hello" should become "olleh".
 */
const reverseString = str => str.split('').reverse().join('')

/** #3
 * Factorialize a Number
    Return the factorial of the provided integer.
    If the integer is represented with the letter n, 
    a factorial is the product of all positive integers less than or equal to n.
    Factorials are often represented with the shorthand notation n!
    For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
    Only integers greater than or equal to zero will be supplied to the function.
 */
const factorialize = num => {
    if (num == 0 || num == 1) {
        return 1
    }
    return num * factorialize(num -1)
    }
    
factorialize(5)

/** #4
 *Find the Longest Word in a String
    Return the length of the longest word in the provided sentence.
    response should be a number.
 */
function findLongestWordLength(str) {
    const makeDo = str.split(' ')
    const strLengths = makeDo.map(item => item.length )
    return Math.max(...strLengths)
  }
  
findLongestWordLength("The quick brown fox jumped over the lazy dog") 
  
  
  /**#5
 * Return Largest Numbers in Arrays
    Return an array consisting of the largest number from each provided sub-array. 
*/
const largestOfFour = arr => arr.map(subA => Math.max(...subA))
  
//console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]))  //passed
let test = [[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]
//console.log(Math.max(...test[0])) //passed

  /**#6
 * Confirm the Ending
    Check if a string (first argument, str) ends with the given target string (second argument, target).
 */
const confirmEnding = (str, target) => str.substring(str.length-(target.length)) == target
    
confirmEnding("Bastian", "n") 

  /**#7 
 * Repeat a String Repeat a String
    Repeat a given string str (first argument) for num times (second argument). 
    Return an empty string if num is not a positive number. 
    For the purpose of this challenge, do not use the built-in .repeat() method.
 */
const repeatStringNumTimes = (str, num) => {
    if(num < 0) {
        return ""
    }
    let rep = ""
        for (let i = 0 ; i < num ; i++) {
        rep += str
        }
    // str.repeat(num)
        return rep
    }
    
repeatStringNumTimes("abc", 3) 

/**#8
 * Truncate a String
    Truncate a string (first argument) if it is longer than the given maximum string length (second argument). 
    Return the truncated string with a ... ending.
 */
const truncateString = (str, num) => str.length > num ? 
    str.replace(str.substring(num),"...")
    : str
    
truncateString("A-tisket a-tasket A green and yellow basket", 8) 

  /**#9
 * Finders Keepers
    Create a function that looks through an array arr and returns the first element in it that passes a 'truth test'. 
    This means that given an element x, the 'truth test' is passed if func(x) is true. 
    If no element passes the test, return undefined.
 */
const findElement = (arr, func) => arr.find(func)

findElement([1, 2, 3, 4], num => num % 2 === 0)

  /**#10
 * Boo who?
    Check if a value is classified as a boolean primitive. Return true or false.
    Boolean primitives are true and false.
 */
const booWho = bool => typeof bool === "boolean"
    
booWho(null)

  /**#11
 * Title Case a Sentence
    Return the provided string with the first letter of each word capitalized. 
    Make sure the rest of the word is in lower case.
    */
const titleCase = str => str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(" ")
    
titleCase("I'm a little tea pot")

  /**#12
 * Slice and Splice
    You are given two arrays and an index.
    Copy each element of the first array into the second array, in order.
    Begin inserting elements at index n of the second array.
    Return the resulting array. The input arrays should remain the same after the function runs.
 */
const frankenSplice = (arr1, arr2, n) => {
    const temp = [...arr2]
    temp.splice(n, 0, ...arr1)
    return temp
    }
    
frankenSplice([1, 2, 3], [4, 5, 6], 1)

  /**#13
 * Falsy Bouncer
    Remove all falsy values from an array. 
    Return a new array; do not mutate the original array.
    Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.
 */
const bouncer = arr => {
    //return arr.filter(Boolean)
    const temp = []
    arr.forEach((curr, index, array) => {
        if (!!curr) {
        temp.push(curr)
        }
    } )
    return temp
    }
    
bouncer([7, "ate", "", false, 9])

  /**#14
 * Where do I Belong
    Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. 
    The returned value should be a number.
    For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater than 1 (index 0), but less than 2 (index 1).
    Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the array has been sorted it will look like [3,5,20] and 19 is less than 20 (index 2) and greater than 5 (index 1).
    */
const getIndexToIns = (arr, num) => {
    const temp = arr.sort((a,b) => a - b)
    let index = 0;
    while (index < arr.length && num > arr[index]) {
        index++;
    }
    return index
    }
    
getIndexToIns([40, 60], 50);

  /**#15
 * Mutations
    Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.
    For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.
    The arguments ["hello", "hey"] should return false because the string hello does not contain a y.
    Lastly, ["Alien", "line"], should return true because all of the letters in line are present in Alien.
 */
const mutation = arr => {
    const str1 = arr[0].toLowerCase(); 
    const str2 = arr[1].toLowerCase(); 
    for (let i = 0; i < str2.length; i++) {
        if (str1.indexOf(str2[i]) === -1) {
            return false; 
        }
    }
    return true;
}

mutation(["hello", "hey"])


  /**#16
 * Chunky Monkey
    Write a function that splits an array (first argument) into groups 
    the length of size (second argument) and returns them as a two-dimensional array.
 */
const chunkArrayInGroups = (arr, size) => {
    const temp = [];
    for (let i = 0; i < arr.length; i += size) {
        temp.push(arr.slice(i, i + size));
    }
    return temp;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
  
  /**
 * 
 */

  /**
 * 
 */
  /**
 * 
 */
  /**
 * 
 */
  /**
 * 
 */
  /**
 * 
 */