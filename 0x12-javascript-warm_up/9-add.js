#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const argument = process.argv.length;
if (argument[2] === NaN || argument === 2) {
  console.log(NaN);
} else {
  console.log(add(Number(process.argv[2]), Number(process.argv[3])));
}
