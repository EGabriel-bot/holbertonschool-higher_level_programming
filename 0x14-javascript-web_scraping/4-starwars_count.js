#!/usr/bin/node
const axios = require('axios');
let appearance = 0;
axios.get(process.argv[2])
  .then(res => {
    for (let blockIndex = 0; blockIndex < res.data.results.length; blockIndex++) {
      if (res.data.results[blockIndex]){
        for (let characterIndex = 0; characterIndex < res.data.results[blockIndex].characters.length; characterIndex++){
          if (res.data.results[blockIndex].characters[characterIndex].includes('18')) {
              appearance++;
        };
        };
      };
    };
    console.log(appearance)
  })
  .catch(error => {
    if (error.response) {
      console.log(`code: ${error.response.status}`);
    }
  });
