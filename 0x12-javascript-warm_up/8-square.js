#!/usr/bin/node
const process = require('process');
const x = parseInt(process.argv[2]);
const message = 'Missing size';
if (isNaN(x)) {
  console.log(message);
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
