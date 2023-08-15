#!/usr/bin/node
// This file defines a class named Rectangle using the class notation.
// The class constructor takes two arguments w (width) and h (height).
// The constructor initializes the instance attributes width and height
// with the provided values of w and h respectively.

module.exports = Rectangle;
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
}
