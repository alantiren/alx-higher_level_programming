#!/usr/bin/node
// Define the factorial function recursively
// Base case: factorial of 0 or 1 is 1
// Recursive case: factorial of n is n times factorial of (n - 1)
// Get the argument
// Convert the argument to an integer
// Check if the argument is a valid integer
// Factorial of NaN is 1
// Factorial of a negative number is Infinity
// Call the factorial function and print the result
function factorial(n) {
  
  if (n === 0 || n === 1) {
    return 1;
  }
  
  return n * factorial(n - 1);
}
const arg = process.argv[2];
const num = parseInt(arg);
if (isNaN(num)) {
  console.log(1);
} else if (num < 0) {
  console.log("Infinity");
} else {
  console.log(factorial(num));
}
