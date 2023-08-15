#!/usr/bin/node
// This file defines a class named Rectangle using the class notation.
// The class constructor takes two arguments w (width) and h (height).
// The constructor initializes the instance attributes width and height
// with the provided values of w and h. If w or h is equal to 0 or not
// a positive integer, an empty object is created.
// It also defines instance methods: print(), rotate(), and double().

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
