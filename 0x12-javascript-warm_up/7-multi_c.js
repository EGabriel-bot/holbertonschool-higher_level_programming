#!/usr/bin/node
const times = process.argv[2];
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < times; i++) {
  console.log('C is fun');
}
