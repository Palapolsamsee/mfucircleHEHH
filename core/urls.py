# <<<<<<< HEAD

from .views import home
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
#commit
urlpatterns = [
    # path('', include(router.urls)),
    path('', home, name='home'), 
    # path('', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tweet/new/', views.create_tweet, name='create_tweet'),
    path('tweet/<int:tweet_id>/comment/', views.create_comment, name='create_comment'),
    path('api/', include(router.urls)),
    path('accounts/profile/', views.profile, name='profile'),
    path('add_comment/<int:tweet_id>/', views.add_comment, name='add_comment'),
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('tweets/', views.all_tweet, name='all_tweet'),
    path('all/',views.all_tweet , name='all_tweets'),
    path('like_tweet/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('like/<int:tweet_id>/', like_tweet, name='like_tweet'),
    path('home/', views.create_tweet, name='create_tweet'),
    path('search/', search_tweets, name='search'),
    # path('search/', home, name='search'),  # เพิ่มเส้นทางนี้
    path('popular/', views.popular_tweets, name='popular_tweets'),
    
]
