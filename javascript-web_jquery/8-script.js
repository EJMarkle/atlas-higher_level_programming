$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach(function (movie) {
    const title = movie.title;
    const listItem = $('<li>').text(title);
    $('#list_movies').append(listItem);
  });
});
