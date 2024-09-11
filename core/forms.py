from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'anonymous']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),
            'anonymous': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
        labels = {
            'anonymous': 'Post as Anonymous',
        }

        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False) 
    
    
        
# class TweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['content']
