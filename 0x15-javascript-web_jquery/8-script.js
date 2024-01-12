$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
    for (const result of data.results) {
      $('#list_movies').append(`<li>${result.title}</li>`);
    }
    console.log(status);
  });
});
