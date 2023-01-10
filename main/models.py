from django.db import models
from django.urls import reverse


class Games(models.Model):
    game_name = models.CharField('Название', max_length=32)
    about_game = models.TextField('Описание')
    download_link = models.CharField('Ссылка для скачивания', max_length=128)
    game_icon = models.ImageField('Иконка', upload_to="photos/%Y/%m/")


    def __str__(self):
        return self.game_name



    def get_absolute_url(self):
        return reverse('game', kwargs={'game_id': self.pk})