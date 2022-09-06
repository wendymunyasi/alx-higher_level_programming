#!/usr/bin/node

/**
 * script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence.
 * Your script must import dict from the file 101-data.js.
 * In the new dictionary: A key is a number of occurrences, a value is
 * the list of user ids.
 * Print the new dictionary at the end
 */
const initDict = require('./101-data').dict;
const newDict = {};

for (const key in initDict) {
  if (newDict[initDict[key]] === undefined) {
    newDict[initDict[key]] = [];
  }
  newDict[initDict[key]].push(key);
}
console.log(newDict);
