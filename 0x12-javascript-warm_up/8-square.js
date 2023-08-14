#!/usr/bin/node
// Get the first argument
// Attempt to convert the argument to an integer
// Check if the conversion was successful and the argument is a positive integer
// Loop to print the square

const arg = process.argv[2];  
const size = parseInt(arg);
if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let row = "";
    for (let j = 0; j < size; j++) {
      row += "X";
    }
    console.log(row);
  }
} else {
  console.log("Missing size");
}
