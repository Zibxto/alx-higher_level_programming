$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
    $('#hello').text(data.hello);
    console.log(status);
  });
});
