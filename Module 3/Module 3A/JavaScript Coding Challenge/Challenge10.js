
// Create a function that filters out negative numbers

const numbers = [1, 0, -43, 5, -7, 20, -77, 9];

function negativeNumber(numbers){
    return numbers < 0
}
console.log(numbers.filter(negativeNumber));

