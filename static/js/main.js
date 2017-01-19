

function task(id){
  var divname = 'datepick' + id;
  var buttonname = 'check' + id;
  var second_div = document.getElementById(divname);
  var first_button = document.getElementById(buttonname);
  $(first_button).hide();
  $(second_div).show();
}
