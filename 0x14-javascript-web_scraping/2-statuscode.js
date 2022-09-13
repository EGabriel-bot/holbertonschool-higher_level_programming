#!/usr/bin/node
const axios = require('axios');
axios.get(String(process.argv[2]))
  .then(res => {
    console.log(`statusCode: ${res.status}`);
  })
  .catch(error => {
    console.error(error);
  });
