from django.db import models
from django.conf import settings


class New_profile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(verbose_name='Имя пользователя', max_length=15)
    name = models.CharField(verbose_name='Имя', max_length=10)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    email = models.EmailField(verbose_name='Почта', max_length=30)
    feedback = models.CharField(verbose_name='Пожелания, предложения', max_length=5000)
    grade = models.IntegerField(verbose_name='Оценка')

    def __str__(self):
        return f'{self.username}'


class Controler(models.Model):
    contr = models.ForeignKey(New_profile, on_delete=models.CASCADE, related_name='owners')
    packet = models.CharField(verbose_name='Подписка', max_length=10, default='none')
    model = models.CharField(verbose_name='Модель', max_length=10)

    def __str__(self):
        return f'{self.model}'

class Products(models.Model):
    user = models.ForeignKey(New_profile, on_delete=models.CASCADE, verbose_name='Пользователь', default='2')
    prod = models.ForeignKey(Controler, verbose_name='Контроллер', on_delete=models.CASCADE, related_name='system_sh',
                             default='2')
    name = models.CharField(verbose_name='Устройство', max_length=20)
    model = models.CharField(verbose_name='Модель устройства', max_length=10)
    condition = models.CharField(verbose_name='Состояние', max_length=10)

    def __str__(self):
        return f'{self.name}'



class CreateAssembling(models.Model):
    # contr = models.ManyToManyField(Controler, related_name='asses', verbose_name='Контроллер')
    # produ = models.ManyToManyField(Products, related_name='asses', verbose_name='Устройство')
    pass


# Промежуточная Products & CreateAsse
class Assembling(models.Model):
    user = models.ForeignKey(New_profile, related_name='assem', on_delete=models.CASCADE,
                             verbose_name='Пользователь', default='2')
    products = models.ForeignKey(Products, related_name='assem', on_delete=models.CASCADE)
    control = models.ForeignKey(Controler, related_name='assem', on_delete=models.CASCADE)
    creass = models.ForeignKey(CreateAssembling, related_name='assem', on_delete=models.CASCADE)
    quant = models.IntegerField()


class ProductStat(models.Model):
    products = models.ForeignKey(Products, verbose_name='Продукт', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=20)
    number = models.CharField(verbose_name="Номер", max_length=8)
    price = models.DecimalField(verbose_name="Цена", decimal_places=3, max_digits=20)




class Comment(models.Model):
    user = models.ForeignKey(New_profile, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.CharField(verbose_name="Коментарий", max_length=150)
    date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)