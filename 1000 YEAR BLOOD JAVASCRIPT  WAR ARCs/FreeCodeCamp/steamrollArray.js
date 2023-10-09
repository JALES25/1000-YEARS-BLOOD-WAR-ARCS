// Steamroller

// Flatten a nested array. 
// You must account for varying levels of nesting.

function steamrollArray(arr) {
    return arr.reduce((acc, curr) => {
        (Array.isArray(curr))? 
            acc.push(...steamrollArray(curr)) :
            acc.push(curr)
        return acc
    }, [])
}

console.log(steamrollArray([1, [2], [3, [[4]]]]))

console.log(steamrollArray([[["a"]], [["b"]]]))

console.log(steamrollArray([1, [], [3, [[4]]]]))

console.log(steamrollArray([1, {}, [3, [[4]]]]))