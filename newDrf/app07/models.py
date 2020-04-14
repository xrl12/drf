from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(verbose_name='游戏名字',max_length=20)
    status = models.IntegerField(verbose_name='游戏状态')
