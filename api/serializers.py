from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(source='body')

class PostCommentSerializer(serializers.Serializer):
    postId = serializers.IntegerField()
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    content = serializers.CharField(source='body')