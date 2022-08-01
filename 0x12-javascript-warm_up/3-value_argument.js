#!/usr/bin/node
const argument = process.argv.length;
if (argument === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
