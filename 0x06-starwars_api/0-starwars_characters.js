#!/usr/bin/node
// Prints all characters of a Star Wars movie.

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, async (err, response, body) => {
  if (err) {
    console.error('Error fetching movie:', err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode} when fetching movie data`);
    return;
  }

  const charArr = JSON.parse(body).characters;

  try {
    const characterPromises = charArr.map(charUrl => {
      return new Promise((resolve, reject) => {
        request(charUrl, (err, response, body) => {
          if (err) {
            reject('Error fetching character:', err);
          } else if (response.statusCode !== 200) {
            reject(`Error: Received status code ${response.statusCode} when fetching character data`);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    // Wait for all character names to be fetched
    const characters = await Promise.all(characterPromises);

    // Print each character name
    characters.forEach(character => console.log(character));
  } catch (error) {
    console.error('Error:', error);
  }
});
