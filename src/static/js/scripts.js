console.log("Script.js is running!");
window.setTimeout(function () {
  $("#lang-message")
    .fadeTo(500, 0)
    .slideUp(500, function () {
      $(this).remove();
    });
}, 5000);

$(document).ready(function () {
  //custom button for homepage
  console.log("Document is ready!");
  $(".share-btn").click(function (e) {
    $(".networks-5")
      .not($(this).next(".networks-5"))
      .each(function () {
        $(this).removeClass("active");
      });
    $(this).next(".networks-5").toggleClass("active");
    console.log("Share block called!");
  });
});
