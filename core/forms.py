from .models import Event
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import AuthenticationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    
# class TweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
        
#         fields = ['content', 'anonymous']
#         widgets = {
#             'content': forms.Textarea(attrs={'class': 'ckeditor'}),
#             'anonymous': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
#         }
#         labels = {
#             'anonymous': 'Post as Anonymous',
#         }


class TweetForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Tweet
        fields = ['content', 'handle', 'anonymous']
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False) 
        
# class TweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['content']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_image', 'event_date']



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm',
            'placeholder': 'Username or Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm',
            'placeholder': 'Password'
        })
    )