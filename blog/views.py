from django.shortcuts import render, get_object_or_404, reverse
# from django.http import HttpResponse
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    paginate_by = 9

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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

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
