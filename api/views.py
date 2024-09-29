from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.services.blog_service import BlogService
from .serializers import PostSerializer 

blog_service = BlogService()

@api_view(['GET'])
def getPosts(request):
    posts_data = blog_service.get_all_posts()
   # print(posts_data)  # Print the raw data returned
    serializer = PostSerializer(posts_data, many=True)
    return Response(serializer.data)
    