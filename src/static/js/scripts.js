console.log("Script.js is running!")
window.setTimeout(function() {
    $("#lang-message").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 5000);

