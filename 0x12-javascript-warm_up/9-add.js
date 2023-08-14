#!/usr/bin/node
// Define the add function
// Get the first and second arguments
// Check if both arguments are provided
// Call the add function and print the result

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
