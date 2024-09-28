import requests
from decouple import config

class BlogService:
    def __init__(self, api_url=None):
        self.api_url = api_url or config('API_URL')

    def get_all_posts(self):
        return self._fetch_data('/posts')

    def get_post_by_id(self, post_id):
        return self._fetch_data(f'/posts/{post_id}')

    def get_comments_for_post(self, post_id):
        return self._fetch_data(f'/posts/{post_id}/comments')

    def _fetch_data(self, endpoint):
        try:
            response = requests.get(f"{self.api_url}{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {endpoint}: {e}")
            return None