from .forms import CustomLoginForm
from .views import create_event, home
from django.urls import path, include
from .import views
from .views import like_tweet, profile
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views_api import TweetViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'comments', CommentViewSet)
from .views_api import TweetViewSet, CommentViewSet
from .views import search_tweets
from django.conf import settings
from django.conf.urls.static import static
from django import forms
from django.contrib.auth.forms import AuthenticationForm
urlpatterns = [
    # path('', include(router.urls)),
    path('', home, name='home'),
    # path('', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(form_class=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tweet/new/', views.create_tweet, name='create_tweet'),
    path('tweet/<int:tweet_id>/comment/', views.create_comment, name='create_comment'),
    path('api/', include(router.urls)),
    path('accounts/profile/', views.profile, name='profile'),
    path('add_comment/<int:tweet_id>/', views.add_comment, name='add_comment'),
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('all/',views.all_tweet , name='all_tweets'),
    path('like_tweet/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('like/<int:tweet_id>/', like_tweet, name='like_tweet'),
    path('home/', views.create_tweet, name='create_tweet'),
    path('helpcenter/', views.helpcenter_view, name='helpcenter_list'),  # ใช้ชื่อฟังก์ชันที่ถูกต้อง
    # path('home/', views.hello, name='home'),
    path('search/', search_tweets, name='search'),
    # path('search/', home, name='search'),  # เพิ่มเส้นทางนี้
    path('news/', views.news, name='news'),
    path('popular/', views.popular_tweets, name='popular_tweets'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('create-event/', views.create_event, name='create_event'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-event/', views.all_tweet, name='all_tweets'), # Link to the event creation form
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

