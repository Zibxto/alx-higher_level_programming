$(function () {
  $('#add_item').on('click', () => {
    $('.my_list').append('<li>Item</li>');
  });

  $('#clear_list').on('click', () => {
    $('.my_list').empty();
  });
});

$('#remove_item').on('click', () => {
  $('.my_list li:last-child').remove();
});
