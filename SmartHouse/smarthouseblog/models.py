from django.db import models
from core.models import New_profile


class Category(models.Model):
    item = models.CharField(max_length=24, verbose_name='Категории', null=True)

    def __str__(self):
        return f'{self.item}'

class Blog(models.Model):
    username = models.ForeignKey(New_profile, verbose_name='Юзернейм', on_delete=models.PROTECT)
    title = models.CharField(max_length=48, verbose_name='Титл поста')
    text = models.TextField(max_length=448, verbose_name='Тело поста')
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name='Опубликовать')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT, default='2')
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # context = f'{self.title},{self.text},{self.username},{self.date}'
        return f'{self.title}'


class Comments(models.Model):
    post = models.ForeignKey(Blog, verbose_name='К посту', on_delete=models.CASCADE, default='2')
    username = models.ForeignKey(New_profile, verbose_name='Юзернейм', on_delete=models.PROTECT, default='2')
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=224, verbose_name='Коментарий')
    #username = models.ForeignKey("auth.User", on_delete=CASCADE)

    def __str__(self):
        # context = f'{self.title},{self.text},{self.username},{self.date}'
        return f'{self.post.id}'