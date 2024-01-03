#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];

const data = fs.readFileSync(filePath, 'utf-8');
console.log(data);
