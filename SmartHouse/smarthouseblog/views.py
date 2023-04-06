from datetime import datetime
from django.db.models import Avg, Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comments, Category, Cart, Order
from .forms import PostForm, CommentForm
from core.models import New_profile

def statistic():
    products = Blog.objects.all().filter(status=True)
    pop_prod = {}
    for product in products:
        pop_prod[product.title] = product.prod_orders.all().count()
    popular_prod = dict(sorted(pop_prod.items(), key=lambda item: -item[1]))
    return popular_prod
print(statistic())

def raiting(post_pk):
    rai = Comments.objects.values('raiting').filter(post=post_pk).aggregate(Avg('raiting'))
    try:
        # return round(sum([int(i.raiting) for i in rai]) / rai.count(), 2)
        return round(rai['raiting__avg'], 2)
    except:
        return 0


def posts(request):
    # Вариант агрегации через стандартные методы без костылей
    cart = Cart.objects.filter(username__username=request.user).first()
    blog = Blog.objects.values(
        'pk', 'title', 'date', 'date_publication', 'status', 'username__username', 'price'
    ).annotate(Avg('comments__raiting')).filter(status=True)
    categor = Category.objects.values('pk', 'item')
    info = cart.product.values('title')
    context = {'info_delete': info,
               'cart_items': cart.product.count(),
               'items': blog,
               'category': categor,
               'cou': Blog.objects.values('pk').filter(status=True).count(),
               'stat': statistic()
               }
    return render(request, 'smarthouseblog/posts.html', context)


def posts_false(request):
    blog = Blog.objects.values(
        'pk', 'title', 'date', 'date_publication', 'price',
    ).annotate(Avg('comments__raiting')).filter(status=False)
    # info = Blog.objects.filter(status=False)
    categor = Category.objects.values('pk', 'item')
    context = {'items': blog,
               'category': categor,
               'cou': Blog.objects.values('pk').filter(status=False).count(),
               }
    return render(request, 'smarthouseblog/posts.html', context)


def categories(request, categories_pk):

    cart = Cart.objects.filter(username__username=request.user).first()
    info = Blog.objects.values(
        'pk', 'title', 'date', 'date_publication', 'status', 'username__username', 'price', 'category__item'
    ).annotate(Avg('comments__raiting')).filter(category=categories_pk, status=True)
    catego = Category.objects.values('pk', 'item')
    context = {
        'info_delete': cart.product.all(),
        'cart_items': cart.product.count(),
        'items': info,
        'category': catego,
        'cou': Blog.objects.values('pk').filter(category=categories_pk, status=True).count(),
    }
    return render(request, 'smarthouseblog/posts.html', context)


def post(request, post_pk):
    info = Blog.objects.values(
         'pk', 'title', 'date', 'date_publication', 'status', 'username__username', 'price', 'text'
    ).get(pk=post_pk)
    comment = Comments.objects.values('pk', 'username__username', 'raiting', 'date', 'comment'
                                      ).filter(post=post_pk).order_by('-date')
    rai = raiting(post_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form_update = comment_form.save(commit=False)
            comment_form_update.post = Blog.objects.filter(pk=post_pk).first()
            comment_form_update.date = datetime.now()
            comment_form_update.save()
            # Вариант костыля для агрегации через создание дополнительного поля в модели
            # и перезапи значения каждый раз при пуше оценки рейтинга в форме
            Blog.objects.values('pk', 'raiting').filter(pk=post_pk).update(raiting=raiting(post_pk))
            return redirect('post', post_pk=post_pk)
    else:
        comment_form = CommentForm()
    context = {'post': info,
               'comm': comment,
               'count_comm': Comments.objects.values('pk').filter(post=post_pk).count(),
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
    return redirect('posts')


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


def cart_del(request, product_id):
    cart = Cart.objects.filter(username__username=request.user).first()
    cart.product.remove(product_id)
    return redirect('cart_detail')


def cart_del_all(request):
    cart = Cart.objects.filter(username__username=request.user).first()
    cart.product.clear()
    return redirect('cart_detail')


def order(request):
    cart = Cart.objects.filter(username__username=request.user).first()
    products = cart.product.all()
    total_price = products.aggregate(Sum('price'))['price__sum']
    order = Order.objects.create(username=cart.username, total_price=total_price)
    order.products.add(*products)
    cart.product.clear()
    return redirect('order_detail')


def order_detail(request):
    orders = Order.objects.filter(username__username=request.user).order_by('-pk')
    context = {
        'orders': orders,
        'all_price': orders.aggregate(Sum('total_price'))
    }
    return render(request, 'smarthouseblog/order_detail.html', context)


