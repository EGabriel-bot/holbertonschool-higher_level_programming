#!/usr/bin/node
const axios = require('axios');
axios.get(String(process.argv[2]))
  .then(res => {
    console.log(`code: ${res.status}`);
  })
  .catch(error => {
    if (error.response) {
      console.log(`code: ${error.response.status}`);
    }
  });
