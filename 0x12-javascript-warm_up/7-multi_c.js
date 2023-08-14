#!/usr/bin/node
// Get the first argument
// Attempt to convert the argument to an integer
// Check if the conversion was successful and the argument is a positive integer
const arg = process.argv[2];
const numTimes = parseInt(arg);
if (!isNaN(numTimes) && numTimes > 0) {
  // Loop to print the message numTimes times
  for (let i = 0; i < numTimes; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
