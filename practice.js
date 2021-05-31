let _ = require('loadash')

function abc (e, x , b) {
    console.log(e, x, b)
    b.push(e*x)
    console.log()
}

let a = [1, 2, 3, 4, 5];
let x = 2
let b = []
_.forEach(a, _.partialRight(abc,  x, b))
// console.log()