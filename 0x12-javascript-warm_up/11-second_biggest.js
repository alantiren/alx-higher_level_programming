#!/usr/bin/node
// Get the command-line arguments
// Convert the arguments to integers
// Filter out NaN values and duplicates
// Find the second biggest integer
// Print the result

const args = process.argv.slice(2);
const integers = args.map(arg => parseInt(arg));
const uniqueIntegers = [...new Set(integers.filter(num => !isNaN(num)))];
const sortedIntegers = uniqueIntegers.sort((a, b) => b - a);
const secondBiggest = sortedIntegers[1] || 0;
console.log(secondBiggest);
