$(document).ready(function() {
    var toggleHeaderDiv = $("#toggle_header");
    toggleHeaderDiv.click(function() {
      var headerElement = $("header");
      if (headerElement.hasClass("red")) {
        headerElement.removeClass("red").addClass("green");
      } else {
        headerElement.removeClass("green").addClass("red");
      }
    });
  });
 