#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((i, v) => i * v);

console.log(list);
console.log(newList);
