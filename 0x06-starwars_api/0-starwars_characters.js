#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from command-line arguments

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

// Make the request to the API to fetch the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // For each character URL, make a request to get the character name
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  } else {
    console.log(`Error: Failed to retrieve movie data for movie ID ${movieId}`);
  }
});
