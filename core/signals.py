from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comment, Tweet

@receiver(post_save, sender=Comment)
def increase_comment_count(sender, instance, created, **kwargs):
    if created:
        tweet = instance.tweet
        tweet.comment_count = Comment.objects.filter(tweet=tweet).count()
        tweet.save()

@receiver(post_delete, sender=Comment)
def decrease_comment_count(sender, instance, **kwargs):
    tweet = instance.tweet
    tweet.comment_count = Comment.objects.filter(tweet=tweet).count()
    tweet.save()
