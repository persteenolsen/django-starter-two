from django.contrib import admin

# Register your models here.

from example.models.post import Post

from example.models.employee import Employee

admin.site.register(Post)

admin.site.register(Employee)
