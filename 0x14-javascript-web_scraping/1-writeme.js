#!/usr/bin/node
// Write a script that write a string to a file.with
// The first argument is the file path

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
