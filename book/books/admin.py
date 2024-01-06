from django.contrib import admin
from books.models import *


# Register your models here.

admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'slug', 'is_published')
    list_display_links = ('id',  'slug', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    fields = ('title', 'slug')
    exclude = ('slug', )
    prepopulated_fields = {"slug": ("title",)}




class PostsCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
