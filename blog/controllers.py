from .services.blog_service import BlogService

class BlogController:
    def __init__(self, service=None):
        self.service = service or BlogService()

    def get_all_posts(self):
        return self.service.get_all_posts()

    def get_post_details(self, post_id):
        post = self.service.get_post_by_id(post_id)
        comments = self.service.get_comments_for_post(post_id) if post else []
        return post, comments