#!/usr/bin/node
// This file defines a class named Square using the class notation.
// The class constructor takes one argument size.
// It inherits from the Square class defined in 5-square.js.
// The constructor of Square is called using super().

module.exports = Square;
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
