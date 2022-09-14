#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
axios.get(String(process.argv[2]))
  .then(res => {
    fs.writeFile(String(process.argv[3]), res.data, 'utf-8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  })
  .catch(error => {
    if (error.response) {
      console.log(`code: ${error.response.status}`);
    }
  });
