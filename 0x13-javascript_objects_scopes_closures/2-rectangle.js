#!/usr/bin/node
// This file defines a class named Rectangle using the class notation.
// The class constructor takes two arguments w (width) and h (height).
// The constructor initializes the instance attributes width and height
// with the provided values of w and h. If w or h is equal to 0 or not
// a positive integer, an empty object is created.

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
