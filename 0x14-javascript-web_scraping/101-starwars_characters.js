#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.dev/api/films/' + process.argv[2];

function orderedPrint (characters, position) {
  request(characters[position], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (position < characters.length - 1) {
        orderedPrint(characters, position + 1);
      }
    }
  });
}

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    orderedPrint(characters, 0);
  }
});
