const a = [1,2,3,4,5,6,7]

const doble = (x) => {
    if (x == []) 0

    return x[0]+ doble(x[0]+1)
}

const novo = a.map.call(a, x => x*2)


console.log(novo)

console.log(doble(a))