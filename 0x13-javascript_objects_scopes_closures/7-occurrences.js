#!/usr/bin/node
// This file defines a function named nbOccurences that returns the number
// of occurrences of a given searchElement in a list.

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
