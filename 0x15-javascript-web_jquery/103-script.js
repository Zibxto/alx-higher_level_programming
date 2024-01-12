$(function () {
  $('#btn_translate, #language_code').on('click keypress', (e) => {
    if ((e.type === 'keypress' && e.which === 13) || e.type === 'click') {
      const LANG = $('#language_code').val();
      const URL = `https://hellosalut.stefanbohacek.dev/?lang=${LANG}`;
      $.get(URL, (data, status) => {
        $('#hello').text(data.hello);
        console.log(status);
      });
    }
  });
});
