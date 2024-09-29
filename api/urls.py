from django.urls import path
from .views import getPosts

urlpatterns = [
    path('posts/', getPosts, name='get_posts'),
]

