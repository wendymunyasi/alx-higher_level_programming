#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// The first argument is the URL to request
const baseURL = process.argv[2];
// The second argument the file path to store the body response
const bodyResp = process.argv[3];
request(baseURL, (error, response, body) => {
  if (error == null) {
    fs.writeFileSync(bodyResp, body);
  }
});
