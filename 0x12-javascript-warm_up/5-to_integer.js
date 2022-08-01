#!/usr/bin/node
const number = process.argv[2];
if (number === undefined || isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(number)}`);
}
