#!/usr/bin/node
// Get the first argument
// Attempt to convert the argument to an integer
// Check if the conversion was successful

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
