#!/usr/bin/node
// Write a script that displays the status code of a GET request.
// The first argument is the URL to request (GET)

const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  }
  console.log(`code: ${response.statusCode}`);
});
