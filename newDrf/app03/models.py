from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='分类名字',max_length=20)
    def __str__(self):
        return self.id
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField(verbose_name='文章标题',max_length=20)
    nvum = models.IntegerField(verbose_name='浏览量')
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='跟新时间')
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='articles')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(verbose_name='标签名字',max_length=10)
    create_time = models.DateTimeField()
    arts = models.ManyToManyField(to=Article,related_name='tags')