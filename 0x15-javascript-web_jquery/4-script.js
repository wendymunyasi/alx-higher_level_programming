// script that toggles the class of the <header> element when the user
// clicks on the tag DIV#toggle_header
const $ = window.$;
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green red');
});
