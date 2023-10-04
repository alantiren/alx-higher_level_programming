$(document).ready(function() {
    $("#add_item").click(function() {
      var newItem = $("<li>Item</li>");
      $("ul.my_list").append(newItem);
    });
    $("#remove_item").click(function() {
      var listItems = $("ul.my_list li");
      if (listItems.length > 0) {
        listItems.last().remove();
      }
    });
    $("#clear_list").click(function() {
      $("ul.my_list").empty();
    });
  });
