#!/usr/bin/node
const fs = require('fs');
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  console.log(`The string has been written to ${filePath}`);
});
