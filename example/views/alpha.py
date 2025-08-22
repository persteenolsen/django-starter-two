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