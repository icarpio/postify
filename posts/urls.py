from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('posts/<int:pk>/', post_detail_view, name='post_detail'), 
    path('user_posts/', user_posts_view, name='user_posts'),
    path('all_posts/', all_posts_view, name='all_posts'),
]