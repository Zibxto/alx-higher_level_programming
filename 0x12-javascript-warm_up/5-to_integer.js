#!/usr/bin/node

const num = process.argv[2];

if (Number(num)) {
  console.log(`My number: ${Math.floor(num)}`);
} else {
  console.log('Not a number');
}
