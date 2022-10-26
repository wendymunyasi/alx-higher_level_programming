// script that updates the text of the <header> element to New Header!!!
//  when the user clicks on DIV#update_header
const $ = window.$;
$('#update_header').bind('click', function () {
  $('header').replaceWith('New Header!!!');
});
