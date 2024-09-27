import requests
from django.shortcuts import render
from django.conf import settings

def post_list_view(request):
    try:
        response = requests.get(settings.POSTS_API)
        response.raise_for_status()
        posts = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        posts = [] 
    
    return render(request, 'post_list.html', {'posts': posts})