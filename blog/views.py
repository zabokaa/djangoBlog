from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import Post
# from .models import Event


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

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        # the 2nd argument is the template name to render:
        "blog/post_detail.html",
        # context dictionary with key(s):
        {"post": post,
        #  "coder": "Saba Kuch",
         },
    )

# class EventsList(generic.ListView):

#     model = Event
#     template_name = "index.html"
#     paginate_by = 12


# def event_detail(request, event_id):

#     event = get_object_or_404(Event, event_id=event_id)
#     queryset = Event.objects.all()
#     post = get_object_or_404(queryset, event_id=event_id)

#     return render(
#         request,
#         # template name
#         "events/event_detail.html",
#         # context
#          {"event": event}
#     )
