$(function () {
  $('#btn_translate').on('click', () => {
    const LANG = $('#language_code').val();
    const URL = `https://hellosalut.stefanbohacek.dev/?lang=${LANG}`;
    $.get(URL, (data, status) => {
      $('#hello').text(data.hello);
      console.log(status);
    });
  });
});
