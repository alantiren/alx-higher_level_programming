#!/usr/bin/node
// This file defines a class named Square using the class notation.
// The class constructor takes one argument size.
// It inherits from the Square class defined in 5-square.js.
// The constructor of Square is called using super().

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
