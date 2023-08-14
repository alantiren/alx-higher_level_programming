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

#!/usr/bin/node
// computes and prints a factorial

function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
