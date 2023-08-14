#!/usr/bin/node
// Get the first argument
// Attempt to convert the argument to an integer
// Check if the conversion was successful and the argument is a positive integer

const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(lang);
  }
}
