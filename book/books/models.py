from autoslug import AutoSlugField
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=255)
    author = models.TextField(max_length=255)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") #так поле отображается в браузере, но не заполняется автоматически

    author = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('PostsCat', on_delete=models.PROTECT, null=True)
    slug = AutoSlugField(unique=True, verbose_name="URL", populate_from='title')  #так поле заполняется автоматически, но не отображается в браузере

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'


class PostsCat(models.Model):
    name = models.CharField(max_length=355, db_index=True)
    slug = AutoSlugField(unique=True, verbose_name="URL", populate_from='name')

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=355)
    email = models.EmailField(max_length=355)
    text = models.TextField(max_length=2000)