from django.urls import path, include
from .views import posts, post, new_post, post_edit, post_delete, posts_false, post_publick, categories, cart_detail, \
    cart_add, cart_del, cart_del_all, order, order_detail

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('posts/false', posts_false, name='posts_false'),
    path('post/<int:post_pk>', post, name='post'),
    path('post_delete/<int:post_pk>', post_delete, name='post_delete'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('post/publick/<int:post_pk>', post_publick, name='post_publick'),
    path('new_post/', new_post, name='new_post'),
    path('categories/<int:categories_pk>', categories, name='categories'),
    path('cart_detail/', cart_detail,  name='cart_detail'),
    path('cart_add/<int:product_pk>', cart_add, name='cart_add'),
    path('cart_dell/<int:product_id>', cart_del, name='cart_del'),
    path('cart_dell_all/', cart_del_all, name='cart_del_all'),
    path('order/', order, name='order'),
    path('order_detail/', order_detail, name='order_detail'),
]
#
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns