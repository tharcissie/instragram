from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
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

      
