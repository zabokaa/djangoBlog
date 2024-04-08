from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Now we have a decorator above the PostAdmin class; delete the existing Post model registration.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content',]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# This will make the Post model visible on the admin page
# admin.site.register(Post)
admin.site.register(Comment)
