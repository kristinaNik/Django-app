import requests
from django.shortcuts import render
from django.conf import settings
import json

def post_list(request):
    try:
        response = requests.get(f"{settings.API_URL}/posts")
        posts = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        posts = [] 
    
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    try:
        post_response = requests.get(f"{settings.API_URL}/posts/{post_id}")
        post = post_response.json() 
        comments_response = requests.get(f"{settings.API_URL}/posts/{post_id}/comments")
        comments = comments_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch comments: {e}")
        comments = []

    return render(request, 'post_detail.html', {'post': post, 'comments': comments})