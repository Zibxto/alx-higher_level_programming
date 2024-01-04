#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) console.log(error);
  const parsedBody = JSON.parse(body);
  let num = 0;
  for (const results of parsedBody.results) {
    for (const item of results.characters) {
      const id = item.split('/');
      if (id[id.length - 2] === '18') {
        num++;
      }
    }
  }
  console.log(num);
});
