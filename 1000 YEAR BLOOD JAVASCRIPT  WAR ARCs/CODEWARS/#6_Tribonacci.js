/*
  create a fibonacci function that given a signature array/list,
   returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; 
n will always be a non-negative number; 
if n == 0, then return an empty array (except in C return NULL) 
and be ready for anything else which is not clearly specified ;)
*/

export default function tribonacci(signature,n){
  const tribo = signature
  
  if (n < signature.length ) {
    temp = []
    for (let i = 0; i < n ;i++) {
      (n !== 0) ? temp.push(signature[i]) : temp = []
    }
    return temp
  } else if (n >= signature.length) {
      for (let i = signature.length; i <n; i++) {
          tribo.push(signature[i-3]+signature[i-2]+signature[i-1])
      }
      return tribo
  }
}
  
  console.log(tribonacci([1,2,3],5)) //passed
  
  // TODO: expected [ 1, 1, 1, 3 ] to deeply equal [ 1, 1, 1, 3, 5, 9, 17, 31, 57, 105 ] n=10
  
  console.log(tribonacci([1,1,1,3],10))  //passed
  
  
  // TODO: expected [ 1, 1, 1 ] to deeply equal [ 1 ] n=1
  
  console.log(tribonacci([1,1,1,],1)) //passed
  
  // TODO: expected [ 300, 200, 100 ] to deeply equal [] n=0
  
  console.log(tribonacci([300, 200, 100],0)) //passed



  // THIS WAS SUPPOSELY THE TOP BEST PRACTIVE SOLUTION
  /*
    function tribonacci(signature,n){  
      for (var i = 0; i < n-3; i++) { // iterate n times
        signature.push(signature[i] + signature[i+1] + signature[i+2]); // add last 3 array items and push to trib
      }
      return signature.slice(0, n); //return trib - length of n
    }
  */