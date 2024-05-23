#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.error('Error writing to file:', err);
      return;
    }
    console.log('File successfully written:', filePath);
  });
});
