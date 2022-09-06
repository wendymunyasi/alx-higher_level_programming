#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  /**
   * @property {method} charPrint - prints the rectangle using the character c
   * @returns void
   */
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
