#!/usr/bin/node
// This file defines a function named converter that returns a function to
// convert a number from base 10 to another base passed as an argument.

exports.converter = function (base) {
 return function (num) {
  return num.toString(base);
 };
};
