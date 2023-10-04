$(document).ready(function() {
    var addItemDiv = $("#add_item");
    addItemDiv.click(function() {
      var newItem = $("<li>Item</li>");
      $("ul.my_list").append(newItem);
    });
  });
