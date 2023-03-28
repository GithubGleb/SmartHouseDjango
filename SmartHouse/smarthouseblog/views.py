from datetime import datetime
from django.db.models import Avg, Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comments, Category, Cart
from .forms import PostForm, CommentForm
from core.models import New_profile


def raiting(post_pk):
    rai = Comments.objects.filter(post=post_pk)
    try:
        return round(sum([int(i.raiting) for i in rai]) / rai.count(), 2)
    except:
        return 0


def posts(request):
    # Вариант агрегации через стандартные методы без костылей
    blog = Blog.objects.values('pk', 'title', 'date', 'date_publication', 'status', 'username__username', 'price').annotate(
        Avg('comments__raiting')).filter(status=True)
    categories = Category.objects.filter()
    context = {'items': blog,
               'category': categories,
               'cou': Blog.objects.all().filter(status=True).count()
               }
    return render(request, 'smarthouseblog/posts.html', context)


def posts_false(request):
    blog = Blog.objects.values('pk', 'title', 'date', 'date_publication').annotate(Avg('comments__raiting')).filter(
        status=False)
    # info = Blog.objects.filter(status=False)
    categor = Category.objects.all()
    context = {'items': blog,
               'category': categor,
               'cou': Blog.objects.all().filter(status=True).count(),
               }
    return render(request, 'smarthouseblog/posts.html', context)


def categories(request, categories_pk):
    info = Blog.objects.values('pk', 'title', 'date', 'date_publication', 'status', 'username__username', 'price').annotate(
        Avg('comments__raiting')).filter(category=categories_pk, status=True)
    categories = Category.objects.all()
    context = {
        'items': info,
        'category': categories,
        'cou': Blog.objects.all().filter(status=True).count(),
    }
    return render(request, 'smarthouseblog/posts.html', context)


def post(request, post_pk):
    info = Blog.objects.get(pk=post_pk)
    comment = Comments.objects.filter(post=post_pk)
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
               'count_comm': comment.count(),
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
            post.raiting = 0
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


def cart_add(request, product_pk):
    product = Blog.objects.filter(pk=product_pk).first()
    cart = Cart.objects.filter(username__username=request.user).first()
    if cart is None:
        user = New_profile.objects.filter(username=request.user).first()
        cart = Cart.objects.create(username=user)
    cart.product.add(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart.objects.filter(username__username=request.user).first()
    if cart is None:
        user = New_profile.objects.filter(username=request.user).first()
        cart = Cart.objects.create(username=user)
    context = {
        'cart': cart.product.all(),
        'summ': cart.product.aggregate(Sum('price')),
    }
    return render(request, 'smarthouseblog/cart_detail.html', context)
