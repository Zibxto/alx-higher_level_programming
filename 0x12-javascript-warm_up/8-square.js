#!/usr/bin/node

const i = process.argv[2];

if (Number(i)) {
  for (let count = 0; count < Math.floor(i); count++) {
    console.log('X'.repeat(i));
  }
} else {
  console.log('Missing size');
}
