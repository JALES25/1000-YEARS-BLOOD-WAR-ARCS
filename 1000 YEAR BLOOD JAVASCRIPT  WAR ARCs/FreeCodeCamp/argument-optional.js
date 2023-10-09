// Arguments Optional

// Create a function that sums two arguments together. 
// If only one argument is provided, then return a function that expects one argument and returns the sum.

// For example, addTogether(2, 3) should return 5, and addTogether(2) should return a function.

// Calling this returned function with a single argument will then return the sum:

// var sumTwoAnd = addTogether(2);
// sumTwoAnd(3) returns 5.

// If either argument isn't a valid number, return undefined.

function addTogether() {
  // Check if all arguments are numbers
  const areAllNumbers = (...args) => args.every(arg => typeof arg === 'number');

  // Check if only one argument is provided and it's a number
  if (arguments.length === 1 && typeof arguments[0] === 'number') {
    const firstArg = arguments[0];

    // Return a function that expects a second argument
    return function(secondArg) {
      if (typeof secondArg === 'number') {
        return firstArg + secondArg;
      } else {
        return undefined;
      }
    };
  }

  // Check if two valid numbers are provided
  if (areAllNumbers(arguments[0], arguments[1])) {
    return arguments[0] + arguments[1];
  }

  // If none of the conditions are met, return undefined
  return undefined;
}


console.log(addTogether(2, 3)); // 5
console.log(addTogether(2)(3)); // 5
console.log(addTogether(2)); // A function expecting a second argument
console.log(addTogether("2", 3)); // undefined (first argument is not a number)
console.log(addTogether(2, "3")); // undefined (second argument is not a number)
console.log(addTogether("2")(3)); // undefined (first argument is not a number)
