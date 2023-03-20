from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comments, Category
from core.models import New_profile
from .forms import PostForm


def posts(request):
    blog = Blog.objects.filter(status=True)
    categories = Category.objects.filter()
    context = {'items': blog,
               'category': categories
               }
    return render(request, 'smarthouseblog/posts.html', context)

def posts_false(request):
    blog = Blog.objects.filter(status=False)
    context = {'items': blog}
    return render(request, 'smarthouseblog/posts.html', context)

def post(request, post_pk):
    info = Blog.objects.get(pk=post_pk)
    comment = Comments.objects.filter(post=post_pk)
    # category = Category.objects.filter(category=post_pk)
    count_com = len(comment)
    context = {'post': info,
               'comm': comment,
               'count_comm': count_com
               }
    return render(request, 'smarthouseblog/post.html', context)


def new_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'smarthouseblog/new_post.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = New_profile.objects.get(pk=request.user.id)
            post.username = user
            post.date = datetime.now()
            post.date_publication = datetime.now()
            post.save()
            return redirect('post', post_pk=post.pk)


def post_edit(request, post_pk):
    post = get_object_or_404(Blog, pk=post_pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'smarthouseblog/new_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            user = New_profile.objects.get(pk=request.user.id)
            post.username = user
            post.date_publication = datetime.now()
            post.save()
            return redirect('post', post_pk=post.pk)


def post_delete(request, post_pk):
    post = get_object_or_404(Blog, pk=post_pk)
    post.delete()
    return redirect('posts')


def post_publick(request, post_pk):
    post = get_object_or_404(Blog, pk=post_pk)
    post.status = True
    post.save()
    return redirect('post', post_pk=post.pk)


def categories(request, categories_pk):
    info = Blog.objects.filter(category=categories_pk, status=True)
    categories = Category.objects.all()
    context = {
        'items': info,
        'category': categories,
    }
    return render(request, 'smarthouseblog/posts.html', context)