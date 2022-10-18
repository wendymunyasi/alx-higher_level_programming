#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api/films';

//  first argument is the movie ID
const movieId = process.argv[2];

request(`${baseUrl}/${movieId}/`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
