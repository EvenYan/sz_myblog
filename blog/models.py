from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=False)
    views = models.PositiveIntegerField(default=100, null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    name = models.CharField(max_length=100)
    boy_num = models.PositiveIntegerField(default=40)
    girl_num = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(max_length=100, verbose_name="用户名", db_column="姓名")
    email = models.CharField(max_length=100)
    passwd = models.CharField(max_length=400)

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = "用户信息表"


class Student(models.Model):
    name = models.CharField(max_length=100)
    sex = models.BooleanField(default=True)
    grade = models.ForeignKey(Grade)
