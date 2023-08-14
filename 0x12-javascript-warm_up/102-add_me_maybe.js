#!/usr/bin/node
// Import the addMeMaybe function from the 102-add_me_maybe.js file
// Use the addMeMaybe function to increment and call a function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
