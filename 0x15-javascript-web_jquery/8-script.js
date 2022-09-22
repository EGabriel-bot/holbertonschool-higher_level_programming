fetch = $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json'), function(data){
  for( i=0; i < fetch; i++){
    $(`<li>${fetch.data.title}</li>`).appendTo('#list_movies')
  }
}

