from .services import BlogService

class BlogController:
    @staticmethod
    def get_all_posts():
        return BlogService.get_all_posts()

    @staticmethod
    def get_post_details(post_id):
        post = BlogService.get_post_by_id(post_id)
        comments = BlogService.get_comments_for_post(post_id)
        return post, comments