#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const count = films.filter(film => film.characters.includes(wedgeAntillesId)).length;
  console.log(count);
});
