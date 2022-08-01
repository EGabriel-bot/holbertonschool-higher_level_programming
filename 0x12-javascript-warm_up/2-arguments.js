#!/usr/bin/node
const argument = process.argv.length;
if (argument === 2) {
  console.log('No argument');
}
if (argument === 3) {
  console.log('Argument found');
} if (argument > 3) {
  console.log('Arguments found');
}
