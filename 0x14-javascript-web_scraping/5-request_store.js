#!/usr/bin/node
const request = require('request');
const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}
const url = process.argv[2];
const filePath = process.argv[3];
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
      console.log(`Webpage content has been saved to ${filePath}`);
    });
  } else {
    console.error(`Failed to fetch the webpage. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
