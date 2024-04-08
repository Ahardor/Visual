// test
import tax from "./tax.js";

test ( "Testing 0", () => {
    let income = 0
    const expectedTax = 0
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})


test ( "Testing 50000", () => {
    let income = 50000
    const expectedTax = 0
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing 150000", () => {
    let income = 150000
    const expectedTax = 2500
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing 250000", () => {
    let income = 250000
    const expectedTax = 7500
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing 250001", () => {
    let income = 250001
    const expectedTax = 7500.10
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing 1000000", () => {
    let income = 1000000
    // 0 за 100К, еще 7500 за 150К, еще 75К за 750К
    const expectedTax = 82500
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing 1000001", () => {
    let income = 1000001
    const expectedTax = 82500.20
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing -1", () => {
    let income = -1
    const expectedTax = 0
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})

test ( "Testing string", () => {
    let income = "рубль"
    const expectedTax = 0
    let calculatedTax = tax(income)
    expect(calculatedTax).toEqual(expectedTax);
})
