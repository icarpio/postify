from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'), 
    path('all_posts/', all_posts_view, name='all_posts')
    #path('user_posts/', user_posts_view, name='user_posts'),
]
