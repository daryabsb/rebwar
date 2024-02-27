$(document).ready(function () {
  // Get blogs when the page loads
  $.get("/blogs/api/list/", function (data) {
    // Iterate through the blogs and populate the HTML
    $.each(data, function (index, blog) {
      // Format date (you may need to adjust this based on your date format)
      var formattedDate = new Date(blog.created).toLocaleDateString("en-US", { month: "short", day: "numeric" });

      // Generate HTML for each blog
      var blogHtml = `
                <div class="post-block">
                    <div class="meta-box">
                        <p class="meta-date">${formattedDate}</p>
                    </div>
                    <div class="post-img">
                        <a href="blog-single.html" class="imghover">
                            <img src="${blog.image}" class="img-responsive" alt="${blog.title}">
                        </a>
                    </div>
                    <div class="post-content">
                        <h1 class="post-title">
                            <a href="blog-single.html" class="title">${blog.title}</a>
                        </h1>
                        <div class="post-meta mb20">
                            <span class="meta-author"> By <a href="#" class="title">${blog.author.name}</a></span>
                            <span class="meta-comment"> ${blog.comments.length} <a href="#" class="title"> Comments </a></span>
                            <span class="meta-category"><a href="#" class="title">${blog.subject}</a></span>
                        </div>
                        <p class="mb30">${blog.short_description}</p>
                        <a href="blog-single.html" class="btn btn-primary">read more</a>
                    </div>
                </div>`;

      // Append the generated HTML to the container
      $("#blog-container").append(blogHtml);
    });
  });
  var blogId = $("#comment-area").data("blog-id");

  var commentsApiURL = `/blogs/api/${blogId}/comments/`;
  var commentsApiURL = `/blogs/api/${blogId}/comments/`;

  $.get(commentsApiURL, function (data) {
    $.each(data, function (index, comment) {
      var commentFormattedDate = new Date(comment.pub_date).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
      var commentHtml = `<ul class="comment-list listnone">
                    <li class="comment" id="comment" data-comment-id="${comment.id}">
                    <div class="comment-body">
                    <div class="comment-author"><img src="${comment.user.image}"
                    alt="Practice - Orthopaedic Surgeon Website Template"
                    class="comment-thumbnail img-responsive img-circle"> </div>
                    <div class="comment-info">
                    <div class="comment-header">
                    <h4 class="user-title">${comment.user.name}</h4>
                    <div class="comment-meta"><span class="comment-meta-date"> ${commentFormattedDate} </span></div>
                    </div>
                    <div class="comment-content">
                    <p>${comment.text}</p>
                    <a href="#" class="btn-link">reply</a>
                    <span> | </span>
                    <a href="#" class="btn-link">like</a>
                    </div>
                    </div>
                    </div>
                    <div id="replies-${comment.id}"></div>
                    </li>
                    </ul>`;

      $("#comment-area").append(commentHtml);
      if (comment.replies && comment.replies.length > 0) {
        $.each(comment.replies, function (replyIndex, reply) {
          var replyFormattedDate = new Date(reply.pub_date).toLocaleDateString("en-US", {
            year: "numeric",
            month: "long",
            day: "numeric",
          });
          var childCommentNode = `
                                <ul class="childern listnone">
                                <li class="comment">
                                    <div class="comment-body">
                                        <div class="comment-author"><img
                                                src="${reply.user.image}"
                                                alt="Practice - Orthopaedic Surgeon Website Template"
                                                class="comment-thumbnail img-responsive img-circle"> </div>
                                        <div class="comment-info">
                                            <div class="comment-header">
                                                <h4 class="user-title">${reply.user.name}</h4>
                                                <div class="comment-meta"><span
                                                        class="comment-meta-date">${replyFormattedDate}</span>
                                                </div>
                                            </div>
                                            <div class="comment-content">
                                                <p>${reply.text}</p>
                                                <a href="#" class="btn-link">reply</a>
                                                <span> | </span>
                                                <a href="#" class="btn-link">like</a>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                                </ul>
                                `;
          $(`#replies-${comment.id}`).append(childCommentNode);
        });
      }
      console.log(comment);
    });
  });

  // Submit a new comment
  $("#submit-comment").on("click", function () {
    var commentText = $("#comment-text").val();
    $.post("/blogs/1/comments/", { text: commentText }, function (data) {
      // Add the new comment to the list
      $("#comment-list").append("<li>" + data.text + "</li>");
    });
  });
});

function initMap() {
  // Replace YOUR_API_KEY with your actual Google Maps API key
  var apiKey = "AIzaSyBOvBbcbUmSo_S9RCgHhA2xpPRK318LFEs";
  var mapContainer = $("#googleMap");

  // Check if Google Maps API key is provided
  // if (apiKey === 'YOUR_API_KEY') {
  //   mapContainer.html('Please provide a valid Google Maps API key.');
  //   return;
  // }

  // Replace LATITUDE and LONGITUDE with your desired coordinates
  var latitude = 35.573611;
  var longitude = 45.421012;

  // Generate the Google Maps Embed API URL
  var mapUrl = "https://www.google.com/maps/embed/v1/place?key=" + apiKey + "&q=" + latitude + "," + longitude;

  // Embed the map using an iframe
  mapContainer.html(
    '<iframe width="100%" height="100%" frameborder="0" style="border:0" src="' + mapUrl + '" allowfullscreen></iframe>'
  );
}

// Initialize the map when the document is ready
$(document).ready(function () {
  initMap();
});

// POPUP BOOK AN APPOINTMENT
$(document).ready(function () {
  // Initialize Magnific Popup
  $("#open-popup").magnificPopup({
    items: {
      src: "#appointment-popup",
      type: "inline",
    },
    closeBtnInside: true,
  });

  // Handle form submission
  $("#appointment-form").submit(function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Add your form submission logic here
    var name = $("#name").val();
    var email = $("#email").val();

    // Example: You can perform an AJAX request to submit the form data
    // $.ajax({
    //   url: 'your_submission_endpoint',
    //   type: 'POST',
    //   data: { name: name, email: email },
    //   success: function(response) {
    //     // Handle success response
    //   },
    //   error: function(error) {
    //     // Handle error
    //   }
    // });

    // Close the Magnific Popup after form submission
    $.magnificPopup.close();
  });
});

// POPUP SAMPLE

$(document).ready(function () {
  $(".popup-with-form").magnificPopup({
    type: "inline",
    preloader: false,
    focus: "#name",

    // When elemened is focused, some mobile browsers in some cases zoom in
    // It looks not nice, so we disable it:
    callbacks: {
      beforeOpen: function () {
        if ($(window).width() < 700) {
          this.st.focus = false;
        } else {
          this.st.focus = "#name";
        }
      },
    },
  });
});

// POPUP SAMPLE END

/*

bing map api key: Av0A1_U_WYU7h7uKufynKoldlyplZ9gUaEQWEOFFVZG4fe9H8iYBL-mUqibHp97J
google api key: AIzaSyBOvBbcbUmSo_S9RCgHhA2xpPRK318LFEs


var commentHtml = `

<ul class="comment-list listnone">
<li class="comment">
<div class="comment-body  ">
<div class="comment-author"><img src="${comment.user.image}"
alt="Practice - Orthopaedic Surgeon Website Template"
class="img-responsive img-circle"> </div>
<div class="comment-info">
<div class="comment-header">
<h4 class="user-title">${comment.user.name}</h4>
<div class="comment-meta"><span class="comment-meta-date"> ${commentFormattedDate} </span></div>
</div>
<div class="comment-content">
<p>${comment.text}</p>
<a href="#" class="btn-link">reply</a>
</div>
</div>
</div>

</li>
</ul>
`
var childCommentNode = `
 <ul class="childern listnone">
<li class="comment">
    <div class="comment-body">
        <div class="comment-author"><img
                src="/static/vendor/images/user3.jpg"
                alt="Practice - Orthopaedic Surgeon Website Template"
                class="img-responsive img-circle"> </div>
        <div class="comment-info">
            <div class="comment-header">
                <h4 class="user-title">Sean Brierly</h4>
                <div class="comment-meta"><span
                        class="comment-meta-date">February 16, 2017</span>
                </div>
            </div>
            <div class="comment-content">
                <p>Donec ac est ut nulla ricursus at urna a, male suada
                    cursus dmodo enim ut conse ctetur convallis.</p>
                <a href="#" class="btn-link">reply</a>
            </div>
        </div>
    </div>
</li>
</ul>
`

                                */
