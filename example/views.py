from django.http import HttpResponse
from datetime import datetime

from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def me(request):
  template = loader.get_template('me.html')
  return HttpResponse(template.render())

# Working with models
from django.shortcuts import render
from .models import Post

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})