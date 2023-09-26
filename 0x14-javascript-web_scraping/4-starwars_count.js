#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const data = JSON.parse(body);
  let count = 0;
  data.results.forEach((movie) => {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(count);
});
