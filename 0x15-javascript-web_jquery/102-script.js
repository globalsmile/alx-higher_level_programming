$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    let lang_code = $('INPUT#language_code').val();
    $('INPUT#language_code').val('');

    let url = 'https://www.fourtonfish.com/hellosalut/hello/' + lang_code + '%22)&format=json';

    $.get(url, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
