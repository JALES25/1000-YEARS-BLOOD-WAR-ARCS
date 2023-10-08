// Convert HTML Entities

// Convert the characters &, <, >, " (double quote), and ' (apostrophe), 
// in a string to their corresponding HTML entities.

function convertHTML(str) {
    const entities = {
      "&": 	"&amp;", 	
      "<": "&lt;", 	
      ">": "&gt;", 
      "\"": "&quot;", 	
      // " ": "&nbsp;", 	
      "–": 	"&ndash;", 	
      "—": 	"&mdash;", 	
      "©": 	"&copy;", 	
      "®": 	"&reg;", 	
      "™": 	"&trade;", 	
      "≈": 	"&asymp;", 	
      "≠": "&ne;", 	
      "£": 	"&pound;", 	
      "€": 	"&euro;", 	
      "°": 	"&deg;",
      "'":  "&apos;",
    }
    return str.split('').map(item => (entities.hasOwnProperty(item))? entities[item] : item).join('')
  }
  
  console.log(convertHTML("Dolce & Gabbana"))
  console.log(convertHTML("Hamburgers < Pizza < Tacos"))
  
  
  
  
      