from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(verbose_name='游戏名字',max_length=20)
    desc = models.CharField(verbose_name='游戏描述',max_length=256)
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
