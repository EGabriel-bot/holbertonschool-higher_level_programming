#!/usr/bin/node
const fs = require('fs');

const content1 = fs.readFileSync(process.argv[2], 'utf-8');
const content2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], content1 + content2);
