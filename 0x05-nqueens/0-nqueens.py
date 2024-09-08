#!/usr/bin/node

// Import the request module to make HTTP requests
const request = require('request');

// Function to print characters in the correct order using recursion
function order(characters, idx) {
  if (idx >= characters.length) {
    return; // Base case: if index is out of bounds, stop recursion
  }
  
  // Request the character details from the character URL
  request(characters[idx], function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      const person = JSON.parse(body); // Parse the character data
      console.log(person.name); // Print the character's name
      order(characters, idx + 1); // Recurse for the next character
    } else {
      console.log('Error occurred, Status code: ' + response.statusCode);
    }
  });
}

// Main logic
const ep = process.argv[2]; // Get the movie ID from the command-line argument
if (!ep) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const url = 'https://swapi-api.hbtn.io/api/films/';

// Make the initial request to get the movie data
request(url + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body); // Parse the movie data
    order(movieData.characters, 0); // Call the function to print characters in order
  } else {
    console.log('Error occurred, Status code: ' + response.statusCode);
  }
});
