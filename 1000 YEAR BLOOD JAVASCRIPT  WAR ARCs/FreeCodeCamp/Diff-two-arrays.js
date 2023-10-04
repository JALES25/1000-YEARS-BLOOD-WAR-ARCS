// Diff Two Arrays

// Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. 
// In other words, return the symmetric difference of the two arrays.
// Note: You can return the array with its elements in any order.

const  diffArray = (arr1, arr2) => {
    const newArr = []
    arr2.forEach(num => (!arr1.includes(num))? newArr.push(num): 69 )
    arr1.forEach(num => (!arr2.includes(num))? newArr.push(num): 69 )

    return newArr
}


const diffArray2 = (arr1, arr2) => { //mine has 69 so this one auto sucks n is trash even tho it has better time and space complexity
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
  
    const difference = [...arr1.filter(item => !set2.has(item)), ...arr2.filter(item => !set1.has(item))];
  
    return difference;
  };
  

