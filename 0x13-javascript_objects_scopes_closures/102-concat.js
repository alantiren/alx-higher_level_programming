#!/usr/bin/node
// Get the source file paths and the destination file path from command line arguments
// Read the contents of the source files
// Concatenate the contents of the source files
// Write the concatenated content to the destination file

const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg + sArg);
