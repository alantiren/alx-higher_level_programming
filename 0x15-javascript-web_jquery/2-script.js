$(document).ready(function() {
    var redHeaderDiv = $("#red_header");
    redHeaderDiv.click(function() {
      var headerElement = $("header");
      headerElement.css("color", "#FF0000");
    });
  });
