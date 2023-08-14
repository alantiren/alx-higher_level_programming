#!/usr/bin/node
// Check the number of arguments passed
// Subtract 2 to exclude the "node" and script path arguments
// Print a message based on the number of arguments

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
