#!/usr/bin/node
// star wars api using nodejs

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function sendReq (character_name, index) {
  if (character_name.length === index) {
    return;
  }

  request(character_name[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendReq(character_name, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character_name = JSON.parse(body).characters;

    sendReq(character_name, 0);
  }
});
