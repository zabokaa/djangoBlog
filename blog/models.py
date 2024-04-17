from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# constants
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    This class represents the Post model. It has the following fields:
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # CLoudinary Field ensures that the uploaded img by user is not stored in bulky, but send over to Cloudinary
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    class Meta:
        ordering = ["created_on"]
    # dunder methods always beloow the Meta class
    def __str__(self):
        return f"{self.title} | written by {self.author}"



class Comment(models.Model):
    """
    This class represents the Comment model. It has the following fields:
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
