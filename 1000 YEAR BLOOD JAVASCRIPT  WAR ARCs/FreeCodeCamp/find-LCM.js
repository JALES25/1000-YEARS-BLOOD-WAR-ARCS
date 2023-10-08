// Smallest Common Multiple

// Find the smallest common multiple of the provided parameters that can be evenly divided by both, 
// as well as by all sequential numbers in the range between these parameters.

// The range will be an array of two numbers that will not necessarily be in numerical order.
// For example, 
// if given 1 and 3, 
// find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. 
// The answer here would be 6.


function smallestCommons(arr) {
    arr.sort((a, b) => a - b)
  
    function lcm(a, b) {
          return (a * b) / gcd(a, b);
      }
  
      function gcd(a, b) {
          if (b === 0) {
              return a;
          } else {
              return gcd(b, a % b);
          }
      }
  
      let result = arr[0];
      for (let i = arr[0] + 1; i <= arr[1]; i++) {
          result = lcm(result, i);
      }
  
      return result;
  
  
  }
  
  console.log(smallestCommons([1,5])) // 60
  console.log(smallestCommons([5,1])) // 60
  console.log(smallestCommons([2,10])) // 2520