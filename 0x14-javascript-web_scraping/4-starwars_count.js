#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }

  try {
    const data = JSON.parse(body).results;

    for (let i = 0; i < data.length; ++i) {
      const characters = data[i].characters;

      for (let j = 0; j < characters.length; ++j) {
        const character = characters[j];
        const characterId = character.split('/')[5];

        if (characterId === '18') {
          times += 1;
        }
      }
    }

    console.log(times);
  } catch (e) {
    console.error('Error parsing JSON:', e);
  }
});
