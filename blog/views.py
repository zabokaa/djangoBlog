from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.

# def hello_blog(request):
#     """Return a simple Hello World message."""
#     return HttpResponse("Hello, Blog!")
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=1)
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    # paginate_by = 6 # 6 posts per page
    paginate_by = 3
