from django.urls import path
from .views import getPosts
from .views import getPostDetail
from .views import getPostComments

urlpatterns = [
    path('posts/', getPosts, name='get_posts'),
    path('posts/<int:post_id>/', getPostDetail, name='get_post_details'),
    path('posts/<int:post_id>/comments/', getPostComments, name='get_post_comments')
]

