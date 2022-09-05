#!/usr/bin/node
const process = require('process');
let numOfTimes = parseInt(process.argv[2]);
const message1 = 'Missing number of occurrences';
const message2 = 'C is fun';
if (isNaN(numOfTimes)) {
  console.log(message1);
} else {
  while (numOfTimes > 0) {
    console.log(message2);
    numOfTimes--;
  }
}
