from django.shortcuts import render
from .controllers import BlogController

def post_list(request):
    posts = BlogController.get_all_posts()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post, comments = BlogController.get_post_details(post_id) 
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})