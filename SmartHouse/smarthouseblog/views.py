from django.shortcuts import render
from .models import Blog
from .forms import PostForm


def posts(requests):
    blog = Blog.objects.all()
    context = {'items': blog}
    return render(requests, 'smarthouseblog/posts.html', context)

def post(requests, post_pk):
    info = Blog.objects.get(pk=post_pk)
    context = {'item': info}
    return render(requests, 'smarthouseblog/post.html', context)

def new_post(requests):
    form = PostForm
    return render(requests, 'smarthouseblog/new_post.html', {'form': form})