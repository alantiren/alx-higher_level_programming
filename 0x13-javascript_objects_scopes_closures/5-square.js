#!/usr/bin/node
// This file defines a class named Square using the class notation.
// The class constructor takes one argument size.
// It inherits from the Rectangle class defined in 4-rectangle.js.
// The constructor of Rectangle is called using super().
// Calls the constructor of Rectangle

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}
module.exports = Square;
