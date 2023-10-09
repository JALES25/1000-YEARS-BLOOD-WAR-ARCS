// Cash Register

// Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.

// cid is a 2D array listing available currency.

// The checkCashRegister() function should always return an object with a status key and a change key.

// Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change.

// Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due.

// Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key.

// Currency Unit	Amount
// Penny	$0.01 (PENNY)
// Nickel	$0.05 (NICKEL)
// Dime	$0.1 (DIME)
// Quarter	$0.25 (QUARTER)
// Dollar	$1 (ONE)
// Five Dollars	$5 (FIVE)
// Ten Dollars	$10 (TEN)
// Twenty Dollars	$20 (TWENTY)
// One-hundred Dollars	$100 (ONE HUNDRED)
// See below for an example of a cash-in-drawer array:

// [
//   ["PENNY", 1.01],
//   ["NICKEL", 2.05],
//   ["DIME", 3.1],
//   ["QUARTER", 4.25],
//   ["ONE", 90],
//   ["FIVE", 55],
//   ["TEN", 20],
//   ["TWENTY", 60],
//   ["ONE HUNDRED", 100]
// ]

var denom = [
	{ name: 'ONE HUNDRED', val: 100},
	{ name: 'TWENTY', val: 20},
	{ name: 'TEN', val: 10},
	{ name: 'FIVE', val: 5},
	{ name: 'ONE', val: 1},
	{ name: 'QUARTER', val: 0.25},
	{ name: 'DIME', val: 0.1},
	{ name: 'NICKEL', val: 0.05},
	{ name: 'PENNY', val: 0.01}
];

function checkCashRegister(price, cash, cid) {
    var output = {status: null, change: []};
    var change = cash - price;
    var register = cid.reduce(function(acc, curr) {
        acc.total += curr[1];
        acc[curr[0]] = curr[1];
        return acc;
    }, {total: 0});
    if(register.total === change) {
        output.status = 'CLOSED';
        output.change = cid;
        return output;
    }
    if(register.total < change) {
        output.status = 'INSUFFICIENT_FUNDS';
        return output;
    }
    var change_arr = denom.reduce(function(acc, curr) {
        var value = 0;
        while(register[curr.name] > 0 && change >= curr.val) {
            change -= curr.val;
            register[curr.name] -= curr.val;
            value += curr.val;
            change = Math.round(change * 100) / 100;
        }
        if(value > 0) {
        acc.push([ curr.name, value ]);
        }
        return acc;
    }, []);
    if(change_arr.length < 1 || change > 0) {
        output.status = 'INSUFFICIENT_FUNDS';
        return output;
    }
    output.status = 'OPEN';
    output.change = change_arr;
    return output;
}


function checkCashRegister0(price, cash, cid) { // TOOK TOO LONG SO I FAILED AGAIN...
    let change = (cash > 0)? cash - price : null
    let enoughChange = false
    let output = {status: "INSUFFICIENT_FUNDS", change: []}
  
    let given = []
  
    function getChange(money,cid) {
      let hundreds = 0
      let twenties = 0
      let tens = 0
      let fives = 0
      let ones = 0
      let quarters = 0
      let dimes = 0
      let nickels = 0
      let pennies = 0
      let onHand = money
      if (money >= 100 && cid[8].includes("ONE HUNDRED")) {
        // hundreds += Math.floor(money / 100)
        cid[0][1] -= Math.floor(money / 100)
        onHand -= (money - (Math.floor(money / 100) * 100)) 
        getChange(money - (Math.floor(money / 100) * 100),cid)
  
      }
      if ((money >= 20 && money < 100) && cid[7].includes("TWENTY")) {
        twenties += Math.floor(money / 20)
        onHand -= (money - (Math.floor(money / 20) * 20))
        getChange(money - (Math.floor(money / 20) * 20),cid)
      }
      if ((money >= 10 && money < 20) && cid[6].hasOwnProperty("TEN")) {
        tens += Math.floor(money / 10)
        onHand -= (money - (Math.floor(money / 10) * 10))
        getChange(money - (Math.floor(money / 10) * 10),cid)
      }
      if ((money >= 5 && money < 10) && cid[5].hasOwnProperty("FIVE")) {
        fives += Math.floor(money / 5)
        onHand -= (money - (Math.floor(money / 5) * 5))
        getChange(money - (Math.floor(money / 5) * 5),cid)
      }
      if ((money >= 1 && money < 5) && cid[4].hasOwnProperty("ONE")) {
        ones += Math.floor(money / 1)
        onHand -= (money - (Math.floor(money / 1) * 1)) 
        getChange(money - (Math.floor(money / 1) * 1),cid)
      }
      if ((money >= 0.25 && money < 1) && cid[3].includes("QUARTER")) {
        // quarters += Math.floor(money / 0.25)
        cid[3][1] -= Math.floor(money / 0.25)
        onHand -= money - (Math.floor(money / 0.25) * 0.25)  
        getChange(money - (Math.floor(money / 0.25) * 0.25),cid)
      }
      if ((money >= 0.10 && money < 0.25) && cid[2].includes("DIME")) {
        dimes += Math.floor(money / 0.10)
        onHand -= money - (Math.floor(money / 0.10) * 0.10)  
        getChange(money - (Math.floor(money / 0.10) * 0.10),cid)
      }
      if ((money >= 0.05 && money < 0.10) && cid[1].includes("NICKEL")) {
        nickels += Math.floor(money / 0.05)
        onHand -= money - (Math.floor(money / 0.05) * 0.05)  
        getChange(money - (Math.floor(money / 0.05) * 0.05),cid)
      }
      if ((money >= 0.01 && money < 0.05) && cid[0].includes("PENNY")) {
        // pennies += Math.floor(money / 0.01)
        cid[0][1] = Math.floor(money / 0.01)
        onHand -= money - (Math.floor(money / 0.01) * 0.01)  
        getChange(money - (Math.floor(money / 0.01) * 0.01),cid)
      }
  
  
  
      return onHand
    }
  
     return cid
    
    // if (enoughChange) {
    //   return output = {status: "INSUFFICIENT_FUNDS", change: []}
    // } else if (cid == change) {
    //   return {status: "CLOSED", change: cid}
    // } else {
    //   return {status: "OPEN", change: [...cid]}
    // }
  
    
  }
  
  console.log(checkCashRegister(119.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]))