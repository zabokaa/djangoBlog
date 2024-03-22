from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# This will make the Post model visible on the admin page
admin.site.register(Post)
admin.site.register(Comment)