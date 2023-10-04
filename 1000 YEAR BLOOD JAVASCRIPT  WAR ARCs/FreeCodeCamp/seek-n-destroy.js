// Seek and Destroy

// You will be provided with an initial array as the first argument to the destroyer function, followed by one or more arguments. 
// Remove all elements from the initial array that are of the same value as these arguments.

// The function must accept an indeterminate number of arguments, also known as a variadic function. 
// You can access the additional arguments by adding a rest parameter to the function definition or using the arguments object.

const destroyer = (arr,...args) => arr.filter(num => !args.includes(num))
    
console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3))