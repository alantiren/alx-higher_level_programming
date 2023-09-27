#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
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
    const charactersUrls = movieData.characters;
    fetchAndPrintCharacters(charactersUrls, 0);
  } else {
    console.error(`No characters found for movie ID ${movieId}`);
  }
});
function fetchAndPrintCharacters (charactersUrls, index) {
  if (index >= charactersUrls.length) {
    return;
  }
  const characterUrl = charactersUrls[index];
  request.get(characterUrl, (charError, charResponse, charBody) => {
    if (charError) {
      console.error(charError);
    } else {
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      fetchAndPrintCharacters(charactersUrls, index + 1);
    }
  });
}
