#!/usr/bin/node
let memory = 0;
exports.logMe = function (item)
{
    console.log(`${memory}: ${item}`);
    memory ++;
}