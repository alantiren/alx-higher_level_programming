#!/usr/bin/node
// This file defines a function named esrever that returns the reversed version
// of a given list without using the built-in reverse method.

exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
