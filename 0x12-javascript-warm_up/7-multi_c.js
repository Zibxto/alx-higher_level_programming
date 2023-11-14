#!/usr/bin/node

const i = process.argv[2];

if (Number(i)) {
  for (let count = 0; count < Math.floor(i); count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
