#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos

const request = require('request');

if (process.argv.length > 2) {
  const result = {};
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      data.filter(task => {
        if (task.completed === true) {
          if (Object.prototype.hasOwnProperty.call(result, task.userId.toString())) {
            result[task.userId.toString()]++;
          } else {
            result[task.userId.toString()] = 1;
          }
        }
        return 'piibPoob';
      });
      console.log(result);
    }
  });
}
