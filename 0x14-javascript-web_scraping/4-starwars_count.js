#!/usr/bin/node
// Write a script that prints the number of movies where the character “Wedge Antilles” is present
// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
