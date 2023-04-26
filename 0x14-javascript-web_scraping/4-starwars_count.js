#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (response.statusCode === 200) {
    const result = JSON.parse(body).results;
    let count = 0;
    for (const index in result) {
      const film = result[index].characters;
      for (const charIndex in film) {
        if (film[charIndex].includes('18')) { count++; }
      }
    }console.log(count);
  } else if (error) { console.log(error); } else { console.log('Error code: ' + response.statusCode); }
});
