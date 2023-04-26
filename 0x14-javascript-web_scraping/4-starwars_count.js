#!/usr/bin/node

const request = require('request');
const url = process.argv[2]

request(url, function (error, response, body) {
  if (error) { console.log(error); } else if (response.statusCode === 200) {
    const result = JSON.parse(body).results;
	  let count = 0;
    console.log(result);
  } else { console.log('Error code: ' + response.statusCode); }
});
