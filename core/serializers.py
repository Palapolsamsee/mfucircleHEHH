# from rest_framework import serializers
# from .models import Tweet,Comment

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

# class TweetSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Tweet
#         fields = '__all__'


# class TweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tweet
#         fields = ['id', 'author', 'handle', 'content', 'likes', 'comment_count']

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'tweet', 'author', 'content', 'created_at']
from rest_framework import serializers
from .models import Tweet, Comment

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'handle', 'content', 'likes', 'comment_count','anonymous']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'tweet', 'author', 'content', 'created_at']
