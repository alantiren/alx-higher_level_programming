#!/usr/bin/node
// Check the number of arguments passed
// Subtract 2 to exclude the "node" and script path arguments
// Print a message based on the number of arguments

const numArgs = process.argv.length - 2;
if (numArgs === 0)
{
console.log("No argument");
}
else if (numArgs === 1)
{
console.log("Argument found");
}
else
{
console.log("Arguments found");
}
