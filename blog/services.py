import requests
from django.conf import settings

class BlogService:
    @classmethod
    def get_all_posts(cls):
        try:
            response = requests.get(f"{settings.API_URL}/posts")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            return []

    @classmethod
    def get_post_by_id(cls, post_id):
        try:
            response = requests.get(f"{settings.API_URL}/posts/{post_id}")
            response.raise_for_status()
            return response.json() 
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching post {post_id}: {e}")
            return None

    @classmethod
    def get_comments_for_post(cls, post_id):
        try:
            response = requests.get(f"{settings.API_URL}/posts/{post_id}/comments")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred while fetching comments for post {post_id}: {req_err}")
            return []