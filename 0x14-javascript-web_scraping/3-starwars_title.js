#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
    You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
    You must use the module request
*/
const request = require('request');
const movieId = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/';

request(endpoint + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const jsonBody = JSON.parse(body);
  console.log(jsonBody.title);
});
