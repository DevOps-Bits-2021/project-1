$(".js-navigate").on("click", function() {
  $(".js-navigate").removeClass("disabled");
  var current = $(".recipe.active");
  var findNext = $(current).next(".recipe");
  var findPrev = $(current).prev(".recipe");
  var button = $(this);

  $(current).removeClass("active");
  setTimeout(function() {
    if ($(button).hasClass("js-right")) {
      $(findNext).addClass("active");
      checkForDisable();
    } else if ($(button).hasClass("js-left")) {
      $(findPrev).addClass("active");
      checkForDisable();
    }
  }, 300);
});

function checkForDisable() {
  var current = $(".recipe.active");
  if ($(current).is(".recipe:last")) {
    $(".js-right").addClass("disabled");
  } else if ($(current).is(".recipe:first")) {
    $(".js-left").addClass("disabled");
  }
}
