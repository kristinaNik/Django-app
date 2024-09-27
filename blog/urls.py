from django.urls import path
from .views import post_list_view

#URL conf module
urlpatterns = [
    path('', post_list_view, name='post_list')
]