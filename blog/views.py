from django.shortcuts import render
from .services.blog_service import BlogService

blog_service = BlogService()

def post_list(request):
    posts = blog_service.get_all_posts()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = blog_service.get_post_by_id(post_id)
    comments = blog_service.get_comments_for_post(post_id) if post else []
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})