from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Helpcenter
from .forms import HelpcenterForm
from core.serializers import TweetSerializer
from .models import Tweet, Comment
from django.contrib.auth.models import User
from .forms import SearchForm, TweetForm, UserRegisterForm
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Tweet , News
from django.contrib.auth import login


def fistpage(request):
    return render(request,'into.html')

def home(request):
    return render(request, 'index.html')

def post(request, p_id):
    kpost= "hello Post" 
    return HttpResponse(kpost +":"+ str(p_id))

def event(request):
    events = Event.objects.all().order_by('-event_date')
    return render(request, 'core/event.html', {'events': events})

@login_required
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
def comment_count(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comment_count = tweet.comments.count()  # Use related_name to count comments

    return JsonResponse({
        'comment_count': comment_count,
    })

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            # Redirect to the page you want after creating the tweet
            return redirect('create_tweet')  # หรือคุณสามารถเปลี่ยนเป็นหน้าอื่น เช่น 'home' หรือ 'all_tweet'
    else:
        form = TweetForm()
        tweets = Tweet.objects.all()  # ดึงทวีตทั้งหมดเพื่อแสดงในหน้า
        events = Event.objects.all().order_by('-event_date')
    return render(request, 'core/all_tweets.html', {'form': form, 'tweets': tweets, 'events': events})


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
    tweets = Tweet.objects.all()
    events = Event.objects.all()  # Fetching all events, ordered by event date  # ดึงทวีตทั้งหมดจากฐานข้อมูล
    
    print("All tweet view called")
    
    return render(request, 'core/all_tweets.html', {
        'tweets': tweets,
        'events': events,
        })


@login_required
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = Comment.objects.filter(tweet=tweet)
    
    is_anonymous = tweet.anonymous  # ตรวจสอบว่าเป็น anonymous 

    return render(request, 'core/tweet_detail.html', {'tweet': tweet, 'comments': comments, 'is_anonymous': is_anonymous})


@login_required
def search_tweets(request):
    form = SearchForm(request.GET)
    tweets = []
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            tweets = Tweet.objects.filter(content__icontains=query)
    return render(request, 'core/search_results.html', {'form': form, 'tweets': tweets})


# Restricting event creation to admins in views.py (if needed for a form-based approach)
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required  # Ensures only staff/admins can access this view
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('create_event')  # Redirect to home page or event list
    else:
        form = EventForm()
    return render(request, 'core/create_event.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ทำการล็อกอินให้ผู้ใช้ทันทีหลังลงทะเบียน
            return redirect('login')  # แก้ไขเส้นทางนี้ตามที่ต้องการ
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def all_event(request):
    events = Event.objects.all()  
    
    print("All Event view called")
    
    return render(request, 'core/all_event.html', {
        'events': events,
        })

@login_required
def event_detail(request, news_id):
    events = get_object_or_404(News, id=news_id)
    return render(request, 'core/event_detail.html', {'events': events})



@login_required
def helpcenter_view(request):
    # ดึงข้อมูล Helpcenter ทั้งหมดจากฐานข้อมูล
    helpcenters = Helpcenter.objects.all()  # หรือใช้ฟังก์ชัน filter() ถ้าต้องการกรองข้อมูล

    # สร้างฟอร์มสำหรับสร้าง Helpcenter ใหม่
    form = HelpcenterForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'helpcenter/helpcenter_list.html', {
        'helpcenters': helpcenters,  # ส่งข้อมูล helpcenters ไปยัง template
        'form': form,
    }) 

@login_required
def news_view(request):
    newss = News.objects.all()
    return render(request, 'core/news.html', {'newss': newss})

@login_required
def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'core/news_detail.html', {'news': news})