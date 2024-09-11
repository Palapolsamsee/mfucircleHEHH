from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    handle = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)
    comment_count = models.IntegerField(default=0)
    anonymous = models.BooleanField(default=False) # !! anonymouse MVP!!
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} (@{self.handle}): {self.content} - Likes: {self.likes.count()} - Anonymous: {str(self.anonymous)}'

    def is_author_admin(self):
        return self.author.is_superuser
    
    def popularity_score(self):
        # กำหนดคะแนนเริ่มต้น โดยใช้ไลค์และคอมเมนต์
        base_score = self.likes.count() + (self.comment_count * 2)
        
        # คำนวณอายุของโพสต์เป็นจำนวนชั่วโมง
        post_age_in_hours = (timezone.now() - self.created_at).total_seconds() / 3600
        
        # ใช้สูตรที่ลดคะแนนตามอายุของโพสต์ (ยิ่งโพสต์เก่ายิ่งมีคะแนนน้อยลง)
        age_factor = 1 / math.log(post_age_in_hours + 2)  # ใช้ log เพื่อลดคะแนนแบบช้าๆ
        
        # คะแนนสุดท้าย = คะแนนเริ่มต้น * ตัวคูณอายุโพสต์
        final_score = base_score * age_factor
        return final_score
    
class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented: {self.content}'