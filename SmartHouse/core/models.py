from django.db import models
from django.conf import settings


class New_profile(models.Model):
    """Вывод данных пользователя"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=10)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    username = models.CharField(verbose_name='Имя пользователя', max_length=15)
    email = models.EmailField(verbose_name='Почта', max_length=30)
    feedback = models.CharField(verbose_name='Пожелания, предложения', max_length=5000)
    grade = models.IntegerField(verbose_name='Оценка')

# Create your models here.
