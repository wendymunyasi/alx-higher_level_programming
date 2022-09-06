#!/usr/bin/node
/**
 * function  that prints the number of arguments already printed and the
 * new argument value
 * @param {item} str - argument passed to function
 * @returns void
 */
let narg = 0;
exports.logMe = function (item) {
  console.log(`${narg}: ${item}`);
  narg++;
};
