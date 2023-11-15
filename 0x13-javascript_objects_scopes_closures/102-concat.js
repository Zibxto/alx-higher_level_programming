#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destFile = process.argv[4];

try {
  const file1 = fs.readFileSync(file1Path.toString(), 'utf-8');
  const file2 = fs.readFileSync(file2Path.toString(), 'utf-8');

  const content = file1 + file2;

  fs.writeFileSync(destFile, content);
} catch (err) {
  console.log('Error occured');
  throw err.message;
}
