from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math
import datetime
from django.utils.crypto import get_random_string
from ckeditor.fields import RichTextField
from datetime import date
class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank = True,null = True)
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)
    comment_count = models.IntegerField(default=0)
    anonymous = models.BooleanField(default=False) # !! anonymouse M P!!
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} {self.content} - Likes: {self.likes.count()} - Anonymous: {str(self.anonymous)}'

    def is_author_admin(self):
        return self.author.is_superuser

    def get_comment_count(self):
        return self.comments.count()
    
    def popularity_score(self):
        # !!กำหนดคะแนนเริ่มต้น โดยใช้ไลค์และคอมเมนต์
        base_score = self.likes.count() + (self.comment_count * 2)
        
        #!! คำนวณอายุของโพสต์เป็นจำนวนชั่วโมง
        post_age_in_hours = (timezone.now() - self.created_at).total_seconds() / 3600
        
        # !!ใช้สูตรที่ลดคะแนนตามอายุของโพสต์ (ยิ่งโพสต์เก่ายิ่งมีคะแนนน้อยลง)
        age_factor = 1 / math.log(post_age_in_hours + 2)  # ใช้ log เพื่อลดคะแนนแบบช้าๆ
        
        # !!คะแนนสุดท้าย = คะแนนเริ่มต้น * ตัวคูณอายุโพสต์
        final_score = base_score * age_factor
        return final_score
    
class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented: {self.content}'
    

class Helpcenter(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='helpcenter_images/', null=True, blank=True)
    is_checked = models.BooleanField(default=False)  # Example of boolean field

    def __str__(self):
        return self.text[:50]

    def is_checked_method(self):
        return self.is_checked

class News(models.Model):
    title = models.TextField(100)
    dis = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='News/', null=True, blank=True)
    
    def __str__(self):
        return self.text
    
