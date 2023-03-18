from django.db import models
from core.models import New_profile

class Blog(models.Model):
    username = models.ForeignKey(New_profile, verbose_name='Юзернейм', on_delete=models.PROTECT)
    title = models.CharField(max_length=48, verbose_name='Титл поста')
    text = models.TextField(max_length=448, verbose_name='Тело поста')
    date = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # context = f'{self.title},{self.text},{self.username},{self.date}'
        return f'{self.username}'
