import requests
from django.conf import settings

class BlogService:
    @classmethod
    def get_all_posts(cls):
        response = requests.get(f"{settings.API_URL}/posts")
        if response.status_code == 200:
            return response.json()
        return []

    @classmethod
    def get_post_by_id(cls, post_id):
        response = requests.get(f"{settings.API_URL}/posts/{post_id}")
        if response.status_code == 200:
            return response.json()
        return None

    @classmethod
    def get_comments_for_post(cls, post_id):
        response = requests.get(f"{settings.API_URL}/posts/{post_id}/comments")
        if response.status_code == 200:
            return response.json()
        return []