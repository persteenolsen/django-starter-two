
# Working with models
from django.shortcuts import render, redirect

from example.models.post import Post

# 07-12-2025 - Handeling Blog view
def blog(request):
    
    # 06-08-2025 - The below statement is equal to the SQL:
    # Select * from Post order by created_at DESC
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog.html', {'posts': posts})
