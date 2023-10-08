// Sum All Odd Fibonacci Numbers

// Given a positive integer num, 
// return the sum of all odd Fibonacci numbers that are less than or equal to num.

// The first two numbers in the Fibonacci sequence are 0 and 1. 
// Every additional number in the sequence is the sum of the two previous numbers. 
// The first seven numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5 and 8.

// For example, 
// sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are 1, 1, 3, and 5.


function sumFibs(num) {
  const fibo = [0,1]
  for (let i = 0; fibo[i] + fibo[i + 1] <= num; i++) {
    fibo.push(fibo[i] + fibo[i+1])
  }
  return fibo.reduce((acc, curr) => {
    if (curr % 2 !== 0) {
     return acc + curr
    }
    return acc
      }, 0)

}

console.log(sumFibs(1))
console.log(sumFibs(1000))
console.log(sumFibs(4))
console.log(sumFibs(7))
console.log(sumFibs(10))
