$(document).ready(function() {
    var updateHeaderDiv = $("#update_header");
    updateHeaderDiv.click(function() {
      var headerElement = $("header");
      headerElement.text("New Header!!!");
    });
  });
