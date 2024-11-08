from django.contrib import admin
from .models import Tweet  # Removed the unnecessary comma
from .models import Comment
from django.http import HttpResponseRedirect
from .models import Helpcenter

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'likes_display', 'comment_count')
    search_fields = ('author__username', 'content')
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


class HelpcenterAdmin(admin.ModelAdmin):
    list_display = ['text', 'date', 'is_checked']  # Include 'is_checked' in list_display
admin.site.register(Helpcenter, HelpcenterAdmin)

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['title', 'event_date', 'created_by']
#     readonly_fields = ['created_by']

#     def save_model(self, request, obj, form, change):
#         if not obj.pk:  # Only set created_by during the first save
#             obj.created_by = request.user
#         super().save_model(request, obj, form, change)
