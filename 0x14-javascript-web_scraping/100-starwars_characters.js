#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = "Return of the Jedi"

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error fetching movie details.');
    process.exit(1);
  }

  const movie = JSON.parse(body);
  console.log(`Characters of "${movie.title}":`);

  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, characterBody) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(characterBody);
        console.log(character.name);
      }
    });
  });
});
