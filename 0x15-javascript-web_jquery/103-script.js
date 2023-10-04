$(document).ready(function() {
    // Attach a click event handler to the "Translate" button
    $("#btn_translate").click(fetchTranslation);

    $("#language_code").keyup(function(event) {
      if (event.key === "Enter") {
        fetchTranslation();
      }
    });
  
    function fetchTranslation() {
      var languageCode = $("#language_code").val();

      $.ajax({
        url: "https://www.fourtonfish.com/hellosalut/hello/",
        type: "GET",
        data: {
          lang: languageCode,
        },
        success: function(data) {
          $("#hello").text(data.hello);
        },
        error: function() {
          $("#hello").text("Error: Translation not found");
        },
      });
    }
  });
  