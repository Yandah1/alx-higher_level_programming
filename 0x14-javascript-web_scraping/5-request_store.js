#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file with
// The first argument is the URL to request

const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
