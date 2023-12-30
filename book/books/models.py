from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=255)
    author = models.TextField(max_length=255)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'