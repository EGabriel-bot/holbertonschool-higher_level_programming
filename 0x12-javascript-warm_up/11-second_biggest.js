#!/usr/bin/node
if (process.argv[2] === undefined || process.argv === 2) {
  console.log('0');
} else {
  process.argv.sort((a, b) => b - a);
  console.log(process.argv[3]);
}
