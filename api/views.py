from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.services.blog_service import BlogService
from .serializers import PostSerializer 
from .serializers import PostCommentSerializer

blog_service = BlogService()

@api_view(['GET'])
def getPosts(request):
    posts_data = blog_service.get_all_posts()
    serializer = PostSerializer(posts_data, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getPostDetail(request, post_id):
    post_by_id = blog_service.get_post_by_id(post_id) 
    serializer = PostSerializer(post_by_id) 
    return Response(serializer.data)

@api_view(['GET'])
def getPostComments(request, post_id):
    post_comments = blog_service.get_comments_for_post(post_id)
    if post_comments:
        serializer = PostCommentSerializer(post_comments, many=True)
        return Response(serializer.data)
    return Response({"detail": "Comments not found."}, status=404)