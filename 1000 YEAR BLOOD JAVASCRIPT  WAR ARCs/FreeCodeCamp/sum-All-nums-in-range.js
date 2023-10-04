// Sum All Numbers in a Range

// We'll pass you an array of two numbers. 
// Return the sum of those two numbers plus the sum of all the numbers between them. 
// The lowest number will not always come first.
// For example, 
// sumAll([4,1]) should return 10 because sum of all the numbers between 1 and 4 (both inclusive) is 10.



function sumAll(arr) {
    const numsInBetwn = []
    arr.sort((a,b) => a - b)
    for (let i = arr[0] + 1; i < arr[1]; i++) {
      numsInBetwn.push(i)
    }
    return arr.reduce((acc, curr) => acc + curr) + numsInBetwn.reduce((acc, curr) => acc + curr)
  }
  
  const sumAll2 = (arr) => {
    const [min, max] = arr.sort((a,b) => a - b)
    const numsInBetween = Array.from({length: max - min - 1}, (_, index) => min + index + 1)
    const newArr = [min,...numsInBetween,max]
    return newArr.reduce((acc, curr) => acc + curr,0)
  }
  
  console.log(sumAll([1, 4]))
  
  console.log(sumAll2([5, 10]))