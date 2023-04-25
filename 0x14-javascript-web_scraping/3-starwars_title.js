#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) { console.log(error); } else if (response.statusCode === 200) {
    const response_j = JSON.parse(body);
    console.log(response_j.title);
  } else { console.log('Error code: ' + response.statusCode); }
});
