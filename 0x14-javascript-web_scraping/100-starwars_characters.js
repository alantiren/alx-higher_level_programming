#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const movieData = JSON.parse(body);
  if (movieData.characters && movieData.characters.length > 0) {
    movieData.characters.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(`No characters found for movie ID ${movieId}`);
  }
});
