from django.http import Http404
from django.shortcuts import render
from .services.blog_service import BlogService

blog_service = BlogService()

def post_list(request):
    posts = blog_service.get_all_posts()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = blog_service.get_post_by_id(post_id)
    
    if post is None:
        raise Http404("Post not found")
    
    comments = blog_service.get_comments_for_post(post_id) 
   
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})