$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
      var movies = data.results;
      var listMovies = $("#list_movies");
      $.each(movies, function(index, movie) {
        var listItem = $("<li>").text(movie.title);
        listMovies.append(listItem);
      });
    });
  });
