$(document).ready(function () {
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });

  $('INPUT#btn_translate').on('click', function () {
    let lang_code = $('INPUT#language_code').val();
    $('INPUT#language_code').val('');

    let url = 'https://www.fourtonfish.com/hellosalut/hello/' + lang_code + '%22)&format=json';

    $.get(url, (data) => {
      $('DIV#hello').text(data.query.results.channel.wind.speed);
    });
  });
});
