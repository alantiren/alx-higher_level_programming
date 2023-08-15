#!/usr/bin/node
// Get the source file paths and the destination file path from command line arguments
// Read the contents of the source files
// Concatenate the contents of the source files
// Write the concatenated content to the destination file

const fs = require('fs');
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;
const sourceContent1 = fs.readFileSync(sourceFilePath1, 'utf8');
const sourceContent2 = fs.readFileSync(sourceFilePath2, 'utf8');
const concatenatedContent = sourceContent1 + sourceContent2;
fs.writeFileSync(destinationFilePath, concatenatedContent);
console.log(`Concatenated ${sourceFilePath1} and ${sourceFilePath2} into ${destinationFilePath}`);
