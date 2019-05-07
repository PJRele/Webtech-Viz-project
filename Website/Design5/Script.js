// JavaScript Document

//DROPDOWN MENU 1
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

//DROPDOWN MENU 2
function myFunction2() {
  document.getElementById("myDropdown2").classList.toggle("show");
}

// CLOSE DROPWDOWN
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}
