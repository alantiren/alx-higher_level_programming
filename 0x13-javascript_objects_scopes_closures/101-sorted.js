#!/usr/bin/node
// Create an empty object to store the new dictionary
// Iterate through the original dictionary
// If the occurrences count is not yet a key in the new dictionary, create it
// Push the user id to the corresponding occurrences count
// Print the new dictionary

const { dict } = require('./101-data');

const convertedArr = Object.entries(dict);

const newObj = {};

convertedArr.forEach(element => {
  newObj[element[1]] ? newObj[element[1]].push(element[0]) : newObj[element[1]] = [element[0]];
});

console.log(newObj);
