#!/usr/bin/node
/**
 * function to count number of occurrences in a list
 * @param {list} list - list ti examine
 * @param {number} searchElement - element to search for
 * @returns {number} - the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};
// alternative to arrow function
// list.forEach(function (item) {
//   if (item === searchElement) {
//     i++;
//   }
// });
