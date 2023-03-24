from datetime import datetime

from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comments, Category
from core.models import New_profile
from .forms import PostForm, CommentForm


def raiting(post_pk):
    rai = Comments.objects.filter(post=post_pk)
    try:
        return round(sum([int(i.raiting) for i in rai]) / rai.count(), 2)
    except:
        return 0


def posts(request):
    #Вариант агрегации через стандартные методы без костылей
    blog = Blog.objects.values('pk', 'title', 'date', 'date_publication', 'status', 'username__username').annotate(Avg('comments__raiting')).filter(status=True)
    cou = blog.count()
    categories = Category.objects.filter()
    context = {'items': blog,
               'category': categories,
               'cou': cou
               }
    return render(request, 'smarthouseblog/posts.html', context)


def categories(request, categories_pk):
    info = Blog.objects.filter(category=categories_pk, status=True)
    categories = Category.objects.all()
    cou = info.count()
    context = {
        'items': info,
        'category': categories,
        'cou': cou,
    }
    return render(request, 'smarthouseblog/posts.html', context)


def posts_false(request):
    info = Blog.objects.filter(status=False)
    categor = Category.objects.all()
    cou = info.count()
    context = {'items': info,
               'category': categor,
               'cou': cou}
    return render(request, 'smarthouseblog/posts.html', context)


def post(request, post_pk):
    info = Blog.objects.get(pk=post_pk)
    comment = Comments.objects.filter(post=post_pk)
    count_com = len(comment)
    rai = raiting(post_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = info
            comment.date = datetime.now()
            comment.save()
            # Вариант костыля для агрегации через создание дополнительного поля в модели
            # и перезапи значения каждый раз при пуше оценки рейтинга в форме
            Blog.objects.filter(pk=post_pk).update(raiting=raiting(post_pk))
            return redirect('post', post_pk=post_pk)

    else:
        comment_form = CommentForm()
    context = {'post': info,
               'comm': comment,
               'count_comm': count_com,
               'comment_form': comment_form,
               'rai': rai,
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
