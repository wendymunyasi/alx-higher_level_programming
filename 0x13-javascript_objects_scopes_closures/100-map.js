#!/usr/bin/node
const initList = require('./100-data.js').list;
const newList = initList.map((number, index) => number * index);

console.log(initList);
console.log(newList);

// Below are alternatives to newList function
// const newList = initList.map(function (number, index) {
//   return number * index;
// });

// const newList = initList.map((number, index) => {
//   return number * index;
// });
