#!/usr/bin/node
const axios = require('axios');
let appearance = 0;
axios.get(process.argv[2])
  .then(res => {
    for (let i = 0; i < res.data.count; i++) {
      console.log('enter_loop');
      if (res.data.characters === 'https://swapi-api.hbtn.io/api/people/18/') {
        console.log('enter_if');
        appearance++;
        console.log('increment');
      } else { continue; }
    }
    console.log('not increment');
    console.log(appearance);
  })
  .catch(error => {
    if (error.response) {
      console.log(`code: ${error.response.status}`);
    }
  });
