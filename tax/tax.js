// tax

const brackets = [0, 100000, 250000, 1000000]
const taxRates = [0, 0.05, 0.10, 0.20]

function tax (income) {
    let result = 0

    // заменить if на цикл

    if (income > 100000 && income <= 250000) {
        result = (income - 100000)*0.05
    } else if (income > 250000 && income < 1000000) {
        result = 7500 + (income - 250000)* 0.1
    } else if (income > 250000 && income < 1000000) {
        result = 7500 + (income - 250000)* 0.1
    } else if (income >= 1000000) {
        result = 82500 + (income - 1000000)* 0.2
    }

    return result
}

export default tax