$(document).ready(function () {
    $.ajax({
        url: '/api/posts/',
        method: 'GET', 
        success: function(posts) {
            const postsContainer = $('#posts-container');
            posts.forEach(function(post) {
                const postHTML = `
                    <div class="col-md-4 mb-3">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">${post.title}</h5>
                                <p class="card-text">${post.body.slice(0, 100)}...</p>
                                <a href="/posts/${post.id}/" class="btn btn-primary">Read More</a>
                            </div>
                        </div>
                    </div>
                `;
                postsContainer.append(postHTML);
            });
        },
        error: function(error) {
            console.error('Error fetching posts:', error);
        }
    });
});