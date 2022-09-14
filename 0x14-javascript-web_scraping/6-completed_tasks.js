#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];

axios.get(url).then(function (response) {
  const tasksCompleted = {};
  for (let i = 0; i < response.data.length; i++) {
    const userID = response.data[i].userId;
    if (response.data[i].completed === true) {
      tasksCompleted[userID] = (tasksCompleted[userID] || 0) + 1;
    }
  }
  console.log(tasksCompleted);
})
  .catch(error => {
    if (error.response) {
      console.log(error);
    }
  });
