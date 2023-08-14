#!/usr/bin/node
// Get the first argument
// Attempt to convert the argument to an integer
// Check if the conversion was successful and the argument is a positive integer
// Loop to print the square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
