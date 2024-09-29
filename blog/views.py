from django.http import Http404
from django.shortcuts import render
from .services.blog_service import BlogService

blog_service = BlogService()

def post_list(request):
    return render(request, 'blog/post_list.html')

def post_detail(request, post_id):   
    return render(request, 'blog/post_detail.html', {'post_id': post_id})