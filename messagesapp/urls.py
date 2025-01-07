from django.urls import path
from .views import *

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('conversation/<int:conversation_id>/', view_conversation, name='view_conversation'),
    path('send_message/<int:recipient_id>/', send_message, name='send_message')
]