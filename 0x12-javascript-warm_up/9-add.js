#!/usr/bin/node
// Define the add function
// Get the first and second arguments
// Check if both arguments are provided
// Call the add function and print the result

function add(a, b) {
  return parseInt(a) + parseInt(b);
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 !== undefined && arg2 !== undefined) {

  console.log(add(arg1, arg2));
} else {
  console.log("NaN");
}
