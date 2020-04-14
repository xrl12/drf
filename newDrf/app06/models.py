from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='名字',max_length=20)
    pwd = models.CharField(verbose_name='密码',max_length=255)

class UserToken(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    token = models.CharField(verbose_name='token',max_length=255)
