from django.contrib import admin
from .models import Tweet, Comment


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'handle', 'content', 'likes_display', 'comment_count')
    search_fields = ('author__username', 'handle', 'content')
    list_filter = ('likes',)
    ordering = ('-id',)

    def likes_display(self, obj):
        return obj.likes.count()  # Assuming likes is a ManyToManyField
    likes_display.short_description = 'Likes'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'tweet', 'created_at')
    search_fields = ('author__username', 'content', 'tweet__content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
