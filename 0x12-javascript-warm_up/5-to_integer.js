#!/usr/bin/node
// Get the first argument
// Attempt to convert the argument to an integer
// Check if the conversion was successful
const arg = process.argv[2];
const parsedInt = parseInt(arg);
if (!isNaN(parsedInt))
{
console.log(`My number: ${parsedInt}`);
}
else
{
console.log("Not a number");
}
