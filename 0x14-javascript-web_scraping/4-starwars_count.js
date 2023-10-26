#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

    The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
    Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
    You must use the module request
*/
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  let wedgeCount = 0;
  for (const result of jsonBody.results) {
    for (const charURL of result.characters) {
      if (charURL.split('/').includes('18')) {
        wedgeCount++;
      }
    }
  }
  console.log(wedgeCount);
});
