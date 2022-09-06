#!/usr/bin/node

/**
 * script that concats 2 files.
 * The first argument is the file path of the first source file.
 * The second argument is the file path of the second source file.
 * The third argument is the file path of the destination.
 */
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const dataA = fs.readFileSync(fileA, { encoding: 'utf8' });
const dataB = fs.readFileSync(fileB, { encoding: 'utf8' });
fs.writeFileSync(fileC, dataA + dataB, { encoding: 'utf8' });
