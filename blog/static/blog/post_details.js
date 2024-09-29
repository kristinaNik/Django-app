$(document).ready(function () {
    const postId = $('#post-id').data('postId');

    $.ajax({
        url: `/api/posts/${postId}/`,
        method: 'GET',
        success: function(post) {
            const postHTML = `
                <h1>${post.title}</h1>
                <p>${post.body}</p>
            `;
            $('#post-container').html(postHTML);
            $.ajax({
                url: `/api/posts/${postId}/comments/`,
                method: 'GET',
                success: function(comments) {
                    comments.forEach(comment => {
                        const commentHTML = `
                            <div class="list-group-item">
                                <h5>${comment.author_name} <small>(${comment.email})</small></h5>
                                <p>${comment.body}</p>
                            </div>
                        `;
                        $('#comments-container').append(commentHTML);
                    });
                },
                error: function(error) {
                    console.error('Error fetching comments:', error);
                }
            });
        },
        error: function(error) {
            console.error('Error fetching post details:', error);
        }
    });
});