from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(verbose_name='文章标题',max_length=10)
    content = models.TextField(verbose_name='文章内容')
    nvum = models.IntegerField(verbose_name='浏览量',default=0)




