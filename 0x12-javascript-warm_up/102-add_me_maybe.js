#!/usr/bin/node
// Import the addMeMaybe function from the 102-add_me_maybe.js file
// Use the addMeMaybe function to increment and call a function
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
