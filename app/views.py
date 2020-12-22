from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)



def create_post(request):
    form = PostForm(request.POST or None, files=request.FILES)      
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_post.html', {'form': form})

      
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})