#!/usr/bin/node
/**
 * function to reverse a list
 * @param {list} list - list to examine
 * @returns {number} - the reversed version of a list
 */
exports.esrever = function (list) {
  return list.reverse();
};

// alternative to list.reverse()
// let newList = [];
// let i;
// for (i = list.length - 1; i >= 0; i--) {
//   newList.push(list[i]);
// }
// return newList;
