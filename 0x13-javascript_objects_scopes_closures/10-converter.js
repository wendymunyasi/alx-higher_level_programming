#!/usr/bin/node
/**
 * function that converts a number from base 10 to another base passed
 * as argument
 * @param {number} base - base to examine
 * @returns {any} - the number converted to given base
 */
exports.converter = function (base) {
  function converted (number) {
    return number.toString(base);
  }
  return converted;
};
