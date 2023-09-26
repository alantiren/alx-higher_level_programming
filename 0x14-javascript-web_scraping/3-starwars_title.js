#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const data = JSON.parse(body);
  if (data.title) {
    console.log(data.title);
  } else {
    console.error(`No movie found with ID ${movieId}`);
    process.exit(1);
  }
});
