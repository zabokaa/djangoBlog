from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # urlpattern slug:slug creates a url path of the domain path plus the slug value:
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # PATH CONVERTER captures a portion of the URL as a variable and converts it to an integer:
    # path("<int:event_id>/", views.event_detail, name="event_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
