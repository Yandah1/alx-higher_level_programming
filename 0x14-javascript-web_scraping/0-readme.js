#!/usr/bin/node

const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Ask the user for the file path
rl.question('Enter the file path: ', (filePath) => {
    // Read the content of the file
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading file: ${err.message}`);
        } else {
            // Print the content
            console.log(data);
        }

        // Close the readline interface
        rl.close();
    });
});

