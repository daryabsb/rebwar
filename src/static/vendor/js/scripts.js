$(document).ready(function () {
    // Get blogs when the page loads
    $.get('/blogs/api/list/', function (data) {
        // Iterate through the blogs and populate the HTML
        $.each(data, function (index, blog) {
            // Format date (you may need to adjust this based on your date format)
            var formattedDate = new Date(blog.created).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

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
            $('#blog-container').append(blogHtml);
        });
    });
    var blogId = $('#comment-area').data('blog-id');

    var commentsApiURL = `/blogs/api/${blogId}/comments/`
    var commentsApiURL = `/blogs/api/${blogId}/comments/`

    $.get(commentsApiURL, function(data){
        $.each(data, function (index, comment) {
            var commentFormattedDate = new Date(comment.pub_date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            var commentHtml = `<ul class="comment-list listnone">
                    <li class="comment" id="comment" data-comment-id="${comment.id }">
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

                    $('#comment-area').append(commentHtml);
                    if (comment.replies && comment.replies.length > 0) {
                        $.each(comment.replies, function (replyIndex, reply) {
                            var replyFormattedDate = new Date(reply.pub_date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
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
                                `
                                $(`#replies-${comment.id}`).append(childCommentNode);
                        })
                    }
            console.log(comment)
        });
    });

    // Submit a new comment
    $('#submit-comment').on('click', function () {
        var commentText = $('#comment-text').val();
        $.post('/blogs/1/comments/', { 'text': commentText }, function (data) {
            // Add the new comment to the list
            $('#comment-list').append('<li>' + data.text + '</li>');
        });
    });
});

/*
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