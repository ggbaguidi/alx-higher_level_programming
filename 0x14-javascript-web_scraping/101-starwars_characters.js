#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

    The first argument is the Movie ID - example: 3 = “Return of the Jedi”
    Display one character name by line in the same order of the list “characters” in the /films/ response
    You must use the Star wars API
    You must use the module request

*/
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(url, async (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);

  for (const charURL of result.characters) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, r, body) => {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
