from django.contrib import admin

# Register your models here.

from example.models.posts import Post

from example.models.employees import Employee

admin.site.register(Post)

admin.site.register(Employee)
