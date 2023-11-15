#!/usr/bin/node

const dict = require('./101-data').dict;

// Function to invert the dictionary
function invertDictionary (originalDict) {
  const invertedDict = {};

  for (const userId in originalDict) {
    const occurrences = originalDict[userId];

    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }

    invertedDict[occurrences].push(userId.toString());
  }

  return invertedDict;
}

// Compute the inverted dictionary
const invertedDict = invertDictionary(dict);

// Print the result
console.log(invertedDict);
