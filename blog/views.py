from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.contrib import messages
# from .models import Event
from django.contrib.auth.models import User

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
    #other users can post comments
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
# form functionality for comments
    if request.method == "POST":
        # assign var name comment_form to IM CommentForm class
        # As specified in forms.py, this will be stored in the body field.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #call the comment_form's save method with commit=False
            #Calling the save method with commit=False returns an object that hasn't yet been saved to the database so that we can modify it further. 
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # displaying a success message
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

# This line resets the content of the form to blank so that a user can write a second comment if they wish.
    comment_form = CommentForm()

    return render(
        request,
        # the 2nd argument is the template name to render:
        "blog/post_detail.html",
        # context dictionary with key(s):
        {   "post": post,
        #  "coder": "Saba Kuch",
            "comments": comments,
            # UP info : name comments in the query is not an actual field in the Post model. 
            # Instead, it is he related_name we supplied in the Comment model.
            "comment_count": comment_count,
            "comment_form": comment_form,
         },
    )

def profile_page(request):
    """
        Display profile page for the user.
    """
    user = get_object_or_404(User, user=request.user)
    comments = user.commenter.all()

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
