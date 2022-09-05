#!/usr/bin/node
const process = require('process');
const message = 'No argument';
const arg = process.argv[2];
if (process.argv.length < 3) {
  console.log(message);
} else {
  console.log(arg);
}
