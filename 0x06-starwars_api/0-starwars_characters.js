#!/usr/bin/node

const request = require('request');

// The first argument passed is the Movie ID
const movieId = process.argv[2];

// Base URL for the Star Wars API
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the body as JSON
  const film = JSON.parse(body);

  // Get the list of character URLs
  const characters = film.characters;

  // Create an array of promises for each character request
  const promises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        } else {
          const character = JSON.parse(charBody);
          resolve(character.name);
        }
      });
    });
  });

  // Use Promise.all to wait for all requests to finish and preserve the order
  Promise.all(promises)
    .then(characterNames => {
      characterNames.forEach(name => {
        console.log(name);
      });
    })
    .catch(err => {
      console.error(err);
    });
});
