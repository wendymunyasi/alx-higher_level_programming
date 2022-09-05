#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const array = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
