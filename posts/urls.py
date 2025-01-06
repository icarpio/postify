from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'), 
    path('all_posts/', all_posts_view, name='all_posts'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    #path('user_posts/', user_posts_view, name='user_posts'),
]
