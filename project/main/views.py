from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

def index(req):
    objs = Post.objects.all()    
    return render(req, 'index.html', {'posts': objs})

def post(req, pk):
    obj = Post.objects.get(id=pk)
    return render(req, 'post.html', {'post': obj})

def newpost(req):
    return render(req, 'newpost.html')