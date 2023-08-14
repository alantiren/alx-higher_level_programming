#!/usr/bin/node
// Check if the first argument is defined
// Print the first argument or "No argument" if no argument is passed

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
