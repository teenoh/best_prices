from django.urls import path, include
from .views import handle_item_post

urlpatterns = [
    path('post-item/', handle_item_post),
]
