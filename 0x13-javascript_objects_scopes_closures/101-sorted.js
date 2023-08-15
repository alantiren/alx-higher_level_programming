#!/usr/bin/node
// Create an empty object to store the new dictionary
// Iterate through the original dictionary
// If the occurrences count is not yet a key in the new dictionary, create it
// Push the user id to the corresponding occurrences count
// Print the new dictionary

const { dict } = require('./101-data');
const newDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  

  newDict[occurrences].push(userId);
}

console.log(newDict);
