from django.urls import path, include
from smarthouseblog.views import posts, post, new_post, post_edit, post_delete

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('post/<int:post_pk>', post, name='post'),
    path('post_delete/<int:post_pk>', post_delete, name='post_delete'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('new_post/', new_post, name='new_post'),
]
