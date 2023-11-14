#!/usr/bin/node

function add (n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  } else {
    return (n * add(n - 1));
  }
}

const num = parseInt(process.argv[2]);
console.log(add(num));
