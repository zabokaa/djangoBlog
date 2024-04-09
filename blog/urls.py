from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # urlpattern slug:slug creates a url path of the domain path plus the slug value:
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
