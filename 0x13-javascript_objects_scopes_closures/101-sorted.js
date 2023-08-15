#!/usr/bin/node
// Create an empty object to store the new dictionary
// Iterate through the original dictionary
// If the occurrences count is not yet a key in the new dictionary, create it
// Push the user id to the corresponding occurrences count
// Print the new dictionary

const dict = require('./101-data').dict;
const newDiction = {};

Object.keys(dict).map(function (key, index) {
  if (newDiction[dict[key]] === undefined) {
    newDiction[dict[key]] = [];
  }
  newDiction[dict[key]].push(key);
});

console.log(newDiction);
