#!/usr/bin/node
// Import the callMeMoby function from the 101-call_me_moby.js file
// Use the callMeMoby function to execute

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
