// Roman Numeral Converter

// Convert the given number into a roman numeral.

// Roman numerals -	Arabic numerals
// M	          -  1000
// CM	          -  900
// D	          -  500
// CD	          -  400
// C	          -  100
// XC	          -  90
// L	          -  50
// XL	          -  40
// X	          -  10
// IX	          -  9
// V	          -  5
// IV	          -  4
// I	          -  1
// All roman numerals answers should be provided in upper-case.

function convertToRoman1(num) { // I ADMIT DEFEAT    
    switch(num){
       case 1:
         return "I"
   
       case 2:
         return "II"
   
       case 3:
         return "III"
   
       case 4:
         return "IV"
   
       case 5:
         return "V"
   
       case 6:
         return "VI"
   
       case 7:
         return "VII"
   
       case 8:
         return "VIII"
   
       case 9:
         return "IX" 
   
       case 10:
         return "X"
   
       case 40:
         return "XL"
   
       case 50:
         return "L"
   
       case 90:
         return "XC"
   
       case 100:
         return "C" 
   
       case 400:
         return "CD"
   
       case 500:
         return "D"
   
       case 900:
         return "CM"
   
       case 1000:
         return "M"
   
       default:
         if (num > 1000) {
           let f1 = num / 1000
           let pre = "M".repeat(Math.floor(f1))
           let a = num - Math.floor(f1) * 1000
           if (num % 1000 === 0) {
             return pre
           } else {
             return pre + convertToRoman(a)
           }
         } else if (num >= 11 && num <= 39) {
           // Handle numbers between 11 and 39
           let x = num >= 30 ? "XXX" : "XX"
           let remainder = num - (10 + (num >= 30 ? 30 : 20))
           return "X" + x.slice(0, remainder) + convertToRoman(remainder)
         }
         return ""
       // case num > 1000:
       //   let f1 = num / 1000
       //   let pre = "M".repeat(Math.floor(f1))
       //   let a = num - (Math.floor(f1) * 1000)
       //   if (num % 1000 === 0) {
       //     return pre + convertToRoman(a)
       //   } 
    }
}
   
   

function convertToRoman0(num) { // switched ideas mid coding this ...oh well
    function isDefRoman(n) {
       switch(n){
       case 1:
         return "I"
         break
       case 2:
         return "II"
         break
       case 3:
         return "III"
         break
       case 4:
         return "IV"
         break
       case 5:
         return "V"
         break
       case 6:
         return "VI"
         break
       case 7:
         return "VII"
         break
       case 8:
         return "VIII"
         break
       case 9:
         return "IX" 
         break
       case 10:
         return "X"
         break
       case 40:
         return "XL"
         break
       case 50:
         return "L"
         break
       case 90:
         return "XC"
         break
       case 100:
         return "C" 
         break
       case 400:
         return "CD"
         break
       case 500:
         return "D"
         break
       case 900:
         return "CM"
         break
       case 1000:
         return "CD"
         break
     }
    }
   
   //  let ans = isDefRoman(num)
   
    function snip(n) {
      let big
      let smol
      let snipped
      if (typeof ans !== "string") {
        big = num.toString().split('').slice(0,-1).join('') + 0
        smol =  num.toString().split('').slice(-1).join('')
       
   
     }
    }
   
   return num.toString().split('').slice(0,-1).join('') + 0
   //  return ans
   }
   
function convertToRoman(num) {
const romanNumerals = [
    { value: 1000, numeral: "M" },
    { value: 900, numeral: "CM" },
    { value: 500, numeral: "D" },
    { value: 400, numeral: "CD" },
    { value: 100, numeral: "C" },
    { value: 90, numeral: "XC" },
    { value: 50, numeral: "L" },
    { value: 40, numeral: "XL" },
    { value: 10, numeral: "X" },
    { value: 9, numeral: "IX" },
    { value: 5, numeral: "V" },
    { value: 4, numeral: "IV" },
    { value: 1, numeral: "I" }
];

let result = "";

for (const { value, numeral } of romanNumerals) {
    while (num >= value) {
    result += numeral;
    num -= value;
    }
}

return result;
}
  
console.log(convertToRoman(36));   // "XXXVI"
console.log(convertToRoman(9));    // "IX"
console.log(convertToRoman(2));    // "II"
console.log(convertToRoman(4));    // "IV"
console.log(convertToRoman(798));  // "DCCXCVIII"
console.log(convertToRoman(1004)); // "MIV"
console.log(convertToRoman(1000)); // "M"
console.log(convertToRoman(5000)); // "MMMMM"
  