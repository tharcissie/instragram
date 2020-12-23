from django import forms
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','name', 'caption')

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2', )

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile', 'bio']