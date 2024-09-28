from django.shortcuts import render
from .controllers import BlogController

blog_controller = BlogController()

def post_list(request):
    posts = blog_controller.get_all_posts()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post, comments = blog_controller.get_post_details(post_id)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})