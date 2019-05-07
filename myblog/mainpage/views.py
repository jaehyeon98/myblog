from django.shortcuts import render

from .models import Post

def home(request):
    posts = Post.objects
    context ={
        'posts' : posts,
    }
    return render(request, 'home.html', context)