#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id.

  The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  Only print users with completed task
  You must use the module request
*/
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  const taskCompletedByUser = {};
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  for (const task of jsonBody) {
    if (task.completed) {
      if (taskCompletedByUser[task.userId]) { taskCompletedByUser[task.userId]++; } else { taskCompletedByUser[task.userId] = 1; }
    }
  }
  console.log(taskCompletedByUser);
});
