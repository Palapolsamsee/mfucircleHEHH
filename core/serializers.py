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
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ['id', 'author_name', 'content', 'likes', 'comment_count', 'anonymous']

    def get_author_name(self, obj):
        if obj.anonymous:
            return "Anonymous"
        return obj.author.username
    
    
class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['tweet', 'author_name', 'content', 'created_at']

    def get_author_name(self, obj):
        if obj.tweet.anonymous:
            return "Anonymous"
        return obj.author.username
