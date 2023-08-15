#!/usr/bin/node
// Use the map function to create a new array with values multiplied
// by their index
// Print both the initial list and the new list

const { list } = require('./100-data');
const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
