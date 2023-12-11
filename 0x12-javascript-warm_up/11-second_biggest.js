#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number);
const sortedNumbers = numbers.sort((a, b) => b - a);

console.log(sortedNumbers.length >= 2 ? sortedNumbers[1] : 0);
