from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    GENDER = (('1', '男'), ('2', '女'))
    gender = models.CharField(choices=GENDER, max_length=10, verbose_name='性别')
    phone = models.CharField(verbose_name='手机号', max_length=11)
    pwd = models.CharField(verbose_name='密码', max_length=20)
