// Sum All Primes

// A prime number is a whole number greater than 1 with exactly two divisors: 1 and itself. 
// For example, 2 is a prime number because it is only divisible by 1 and 2. 
// In contrast, 4 is not prime since it is divisible by 1, 2 and 4.

// Rewrite sumPrimes so it returns the sum of all prime numbers that are less than or equal to num.

import isPrime from "./isPrime"

function sumPrimes(num) {
  const arr = Array.from({length:num+1}, (_, index) => index)
  return arr.reduce((acc,curr) => {
    if (isPrime(curr)) {
      return acc + curr
    }
    return acc
  })
}

console.log(sumPrimes(10))
console.log(sumPrimes(977))


// function isPrime(number) {
//   if (number <= 1) {
//     return false; 
//   }
//   if (number <= 3) {
//     return true; 
//   }
//   if (number % 2 === 0 || number % 3 === 0) {
//     return false; 
//   }

//   let i = 5;
//   while (i * i <= number) {
//     if (number % i === 0 || number % (i + 2) === 0) {
//       return false; 
//     }
//     i += 6; 
//   }
//   return true; 
// }