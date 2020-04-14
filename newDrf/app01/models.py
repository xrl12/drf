from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(verbose_name='组名',max_length=20)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(verbose_name='学生姓名',max_length=20)
    age = models.IntegerField(verbose_name='学生年龄')
    gender = (
        ("1","男"),
        ("2","女"),
              )
    genders = models.CharField(verbose_name='学生性别',choices=gender,max_length=20)
    group = models.ForeignKey(to=Group,on_delete=models.CASCADE,related_name='student')

