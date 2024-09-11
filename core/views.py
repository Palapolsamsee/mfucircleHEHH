# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from rest_framework import viewsets
# from .models import Tweet,Comment
# from .serializers import CommentSerializer, TweetSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet, Comment
from django.contrib.auth.models import User
from .forms import SearchForm, TweetForm, UserRegisterForm
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Tweet
from django.contrib.auth import login


def home(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'home.html')

def post(request, p_id):
    kpost= "hello Post" 
    return HttpResponse(kpost +":"+ str(p_id))

def popular_tweets(request):
    # ดึงโพสต์ทั้งหมดแล้วคำนวณคะแนนความนิยม
    tweets = Tweet.objects.all()
    tweets = sorted(tweets, key=lambda tweet: tweet.popularity_score(), reverse=True)

    return render(request, 'core/popular_tweets.html', {'tweets': tweets})

# class TweetViewSet(viewsets.ModelViewSet):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer




@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    user = request.user
    if user in tweet.likes.all():
        tweet.likes.remove(user)
        liked = False
    else:
        tweet.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': tweet.likes.count(),
    })



@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            return redirect('create_tweet') # Redirect to the home page after posting
    else:
        form = TweetForm()
        tweets = Tweet.objects.all()
    return render(request, 'core/all_tweets.html', {'tweets': tweets, 'form': form})

@login_required
def create_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        content = request.POST.get("content")
        comment = Comment.objects.create(
            tweet=tweet,
            author=request.user,
            handle=request.user.username,
            content=content
        )
        return redirect("create_tweet", tweet_id=tweet.id)
    return render(request, "home.html", {"tweet": tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_tweet')  # เปลี่ยน 'home' เป็นชื่อ URL ของหน้าแรกที่คุณต้องการนำผู้ใช้ไปหลังจากลงทะเบียนเสร็จ
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    tweets = Tweet.objects.filter(author=user)  # ดึงทวีตทั้งหมดของผู้ใช้

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Tweet.objects.create(author=user, handle=user.username,content=content)
            return redirect('login')  # หรือชื่อ URL ของหน้าโปรไฟล์
    return render(request, 'core/profile.html', {'tweets': tweets})

@login_required
def add_comment(request, tweet_id):
    if request.method == 'POST':
        tweet = get_object_or_404(Tweet, id=tweet_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(tweet=tweet, author=request.user, content=content)
    return redirect('tweet_detail', tweet_id=tweet_id)

@login_required
def all_tweet(request):
    tweets = Tweet.objects.all()  # ดึงทวีตทั้งหมดจากฐานข้อมูล
    return render(request, 'core/all_tweets.html', {'tweets': tweets})


@login_required
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = Comment.objects.filter(tweet=tweet)
    return render(request, 'core/tweet_detail.html', {'tweet': tweet, 'comments': comments})

@login_required
def search_tweets(request):
    form = SearchForm(request.GET)
    tweets = []
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            tweets = Tweet.objects.filter(content__icontains=query)
    return render(request, 'core/search_results.html', {'form': form, 'tweets': tweets})

