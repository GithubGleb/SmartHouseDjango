from django.urls import path, include
from smarthouseblog.views import posts, post, new_post

urlpatterns = [
    path('blog/', posts, name='posts'),
    path('post/<int:post_pk>', post, name='post'),
    path('new_post/', new_post, name='new_post'),
]
