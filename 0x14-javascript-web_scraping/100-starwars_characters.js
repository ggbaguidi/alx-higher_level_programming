#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
  Display one character name by line
  You must use the Star wars API
  You must use the module request
*/
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

request(url + movieId, (error, response, body) => {
  if (error) { console.log(error); }
  const poeples = JSON.parse(body).characters;
  for (const poepleUrl of poeples) {
    request(poepleUrl, (e, r, b) => {
      if (e) { console.log(e); }
      const name = JSON.parse(b).name;
      console.log(name);
    });
  }
});
