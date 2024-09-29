from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='body')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']