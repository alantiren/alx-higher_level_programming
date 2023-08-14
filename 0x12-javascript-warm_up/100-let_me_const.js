#!/usr/bin/node
// Initialize myVar to 89
// Require and execute the 100-let_me_const.js file
// Print the value of myVar after the modification

myVar = 89;
require('./100-let_me_const');
console.log(myVar);
