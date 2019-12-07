from django.db import models

# Create your models here.

class MyManager(models.Manager):
    def count_title(self, kw):
        return self.filter(title__contains=kw).count()


class NormalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(excerpt__exact='Secret')


class SecretManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(excerpt__exact='Secret')


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=False)
    views = models.PositiveIntegerField(default=100, null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)
    excerpt = models.CharField(max_length=100, default="Normal")
    my_objects = MyManager()
    normal_objects = NormalManager()
    secret_objects = SecretManager()

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


class People(models.Model):
    name = models.CharField(max_length=100)


class IDCard(models.Model):
    num = models.CharField(max_length=18)
    people = models.OneToOneField(People, on_delete=models.PROTECT)
