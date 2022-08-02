#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
      string = '';
    }
  }

  rotate () {
    const newWidth = this.width;
    this.width = this.height;
    this.height = newWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
