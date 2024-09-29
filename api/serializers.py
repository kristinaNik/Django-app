from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=100)

class PostCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    postId = serializers.IntegerField()
    author_name = serializers.CharField(source='name')
    email = serializers.EmailField(max_length=50)
    body = serializers.CharField(max_length=100)