from django.shortcuts import render, redirect

# 11-12-2025 - Returning the Templates like below allow the Logout Menu Item to work properly
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def me(request):
    return render(request, 'me.html')