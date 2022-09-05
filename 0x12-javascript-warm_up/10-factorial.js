#!/usr/bin/node
function factorial (number) {
  if ((isNaN(number)) || (number === 1)) {
    return 1;
  }
  return factorial(number - 1) * number;
}
console.log(factorial(parseInt(process.argv[2])));
