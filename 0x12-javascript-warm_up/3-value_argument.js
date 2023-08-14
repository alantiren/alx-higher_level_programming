#!/usr/bin/node
// Check if the first argument is defined
// Print the first argument or "No argument" if no argument is passed

const firstArg = process.argv[2];
if (firstArg !== undefined)
{
console.log(firstArg);
}
else
{
console.log("No argument");
}
