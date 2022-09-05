#!/usr/bin/node
const process = require('process');
let message;
if (process.argv.length === 3) {
  message = 'Argument found';
} else if (process.argv.length < 3) {
  message = 'No argument';
} else {
  message = 'Arguments found';
}
console.log(message);
