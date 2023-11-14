#!/usr/bin/node

const arr = [];
let i = 0;

if (process.argv.length < 4) {
  console.log(0);
} else {
  while (i < process.argv.length) {
    if (i > 1) {
      arr.push(parseInt(process.argv[i]));
    }
    i++;
  }

  arr.sort((a, b) => {
    return a - b;
  });
  console.log(arr[arr.length - 2]);
}
