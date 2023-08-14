#!/usr/bin/node
// Import the callMeMoby function from the 101-call_me_moby.js file
// Use the callMeMoby function to execute

const callMeMoby = require('./101-call_me_moby').callMeMoby;
 a function 3 times
callMeMoby(3, function () {
  console.log('C is fun');
});
