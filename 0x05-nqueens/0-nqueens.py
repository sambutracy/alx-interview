#!/usr/bin/node

const request = require('request');

// Function to print character names in order
function fetchCharacters(characters, idx) {
  if (idx >= characters.length) {
    return; // Base case: if the index is out of bounds, stop recursion
  }

  // Request the character details from the character URL
  request(characters[idx], (err, response, body) => {
    if (err) {
      console.error(err);
    } else if (response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name); // Print the character's name
      fetchCharacters(characters, idx + 1); // Recurse for the next character
    } else {
      console.error('Failed to retrieve character, status code:', response.statusCode);
    }
  });
}

// Get the Movie ID from the command-line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the URL for the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Fetch the movie data based on the Movie ID
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body); // Parse the movie data
    const characters = movieData.characters; // Get the list of character URLs
    fetchCharacters(characters, 0); // Start fetching characters in order
  } else {
    console.error('Failed to retrieve movie, status code:', response.statusCode);
  }
});
