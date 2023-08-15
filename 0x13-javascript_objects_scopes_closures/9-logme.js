#!/usr/bin/node
// This file defines a function named logMe that prints the number of arguments
// already printed and the new argument value.
// Initialize the counter

let numArguments = 0;

exports.logMe = function (item) {
  console.log(`${numArguments}: ${item}`);
  numArguments++;
};
