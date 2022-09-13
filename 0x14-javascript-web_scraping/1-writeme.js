#!/usr/bin/node
const fs = require('fs');
const data = String(process.argv[3]);
fs.writeFile(String(process.argv[2]), data, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
