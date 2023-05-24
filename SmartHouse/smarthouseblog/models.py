from django.db import models
from core.models import New_profile
from django.utils import timezone


class Category(models.Model):
    item = models.CharField(
        max_length=24,
        verbose_name='Категории',
        null=True
    )

    def __str__(self):
        return f'{self.item}'


class Blog(models.Model):
    username = models.ForeignKey(
        New_profile,
        verbose_name='Юзернейм',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        max_length=48,
        verbose_name='Титл поста (Название устройства)'
    )
    text = models.TextField(
        max_length=448,
        verbose_name='Тело поста'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Опубликовать'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.PROTECT,
        default='2'
    )
    date_publication = models.DateTimeField(
        auto_now_add=True
    )
    raiting = models.FloatField(
        verbose_name='Рейтинг',
        default=0,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,

    )

    def __str__(self):
        # context = f'{self.title},{self.text},{self.username},{self.date}'
        return f'title: {self.title}, username: {self.username}'


class Comments(models.Model):
    post = models.ForeignKey(
        Blog,
        verbose_name='К посту',
        on_delete=models.CASCADE,
        related_name='comments',
        default=2
    )
    username = models.ForeignKey(New_profile,
                                 verbose_name='Юзернейм',
                                 on_delete=models.PROTECT,
                                 default='2',
                                 related_name='users')
    date = models.DateTimeField(
        auto_now_add=True
    )
    comment = models.TextField(
        max_length=224,
        verbose_name='Коментарий'
    )
    raiting = models.IntegerField(
        verbose_name='Рейтинг',
        # choices=list_star,
        blank=False,
        default=0,

    )

    def __str__(self):
        return f'{self.raiting}'


class Card(models.Model):
    number = models.CharField(
        max_length=12,
        verbose_name='Номер карты'
    )
    num_date = models.CharField(
        max_length=4,
        verbose_name='Срок действия'
    )
    name = models.TextField(
        max_length=8,
        verbose_name='Имя'

    )
    surname = models.CharField(
        max_length=23,
        verbose_name='Фамилия'
    )


class Cart(models.Model):
    username = models.ForeignKey(
        New_profile,
        related_name='user',
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        Blog,
        related_name='product',
    )


class Order(models.Model):
    username = models.ForeignKey(
        New_profile,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(
        Blog,
        related_name='prod_orders',
    )
    condition = models.TextField(
        max_length=12,
        verbose_name='Cостояние',
        default='Передано на сборку.',
    )
    date_order = models.DateTimeField(
        auto_now_add=True
    )
    date_dilivery = models.DateTimeField(
        default=timezone.now
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return f'{self.username}, {self.total_price}'
