from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet ,Helpcenter
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
        fields = ['content', 'anonymous']
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False) 
        
# class TweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['content']


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


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': 'Your username',
                'required': 'true'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': 'name@company.com',
                'required': 'true'
            }),
        }

    # ตั้งค่า widgets สำหรับ password fields โดยตรง
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
            'placeholder': '••••••••',
            'required': 'true'
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
            'placeholder': '••••••••',
            'required': 'true'
        }),
    )

class HelpcenterForm(forms.ModelForm):
    class Meta:
        model = Helpcenter
        fields = ['text', 'image']  # Exclude 'date' because it's auto-generated