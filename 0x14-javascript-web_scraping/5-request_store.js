#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file.

    The first argument is the URL to request
    The second argument the file path to store the body response
    The file must be UTF-8 encoded
    You must use the module request
*/
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url + '/' + path, (error, response, body) => {
  if (error) { console.log(error); }
  fs.writeFile(path, body, 'utf-8', (error) => {
    if (error) { console.log(error); }
  });
});
