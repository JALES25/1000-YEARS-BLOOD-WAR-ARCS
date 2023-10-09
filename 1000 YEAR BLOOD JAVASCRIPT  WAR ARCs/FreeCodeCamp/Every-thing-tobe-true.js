// Everything Be True

// Check if the predicate (second argument) is truthy on all elements of a collection (first argument).

// In other words, you are given an array collection of objects. 
// The predicate pre will be an object property and you need to return true if its value is truthy. 
// Otherwise, return false.
// In JavaScript, truthy values are values that translate to true when evaluated in a Boolean context.

function truthCheck(collection, pre) {
    return collection.every(obj => obj.hasOwnProperty(pre) && Boolean(obj[pre]))
  }
  
console.log(truthCheck([{name: "Quincy", role: "Founder", isBot: false}, {name: "Naomi", role: "", isBot: false}, {name: "Camperbot", role: "Bot", isBot: true}], "isBot"))

console.log(truthCheck([{name: "Quincy", role: "Founder", isBot: false}, {name: "Naomi", role: "", isBot: false}, {name: "Camperbot", role: "Bot", isBot: true}], "name"))

console.log(truthCheck([{name: "Quincy", role: "Founder", isBot: false}, {name: "Naomi", role: "", isBot: false}, {name: "Camperbot", role: "Bot", isBot: true}], "role") )

console.log(truthCheck([{name: "Pikachu", number: 25, caught: 3}, {name: "Togepi", number: 175, caught: 1}], "number"))