// Spinal Tap Case

// Convert a string to spinal case. 
// Spinal case is all-lowercase-words-joined-by-dashes.


function spinalCase(str) {//this one destroyed me (imagine doing mind gymnastics to end up coming up with some bug then 1 quick search destroys you)
    
    // Create a variable for the white space and underscores.
  var regex = /\s+|_+/g;

  // Replace low-upper case to low-space-uppercase
  str = str.replace(/([a-z])([A-Z])/g, "$1 $2");

  // Replace space and underscore with -
  return str.replace(regex, "-").toLowerCase();
}

console.log(spinalCase('This Is Spinal Tap'))
console.log(spinalCase("thisIsSpinalTap"))
console.log(spinalCase("Teletubbies say Eh-oh"))