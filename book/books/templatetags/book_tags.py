from django import template
from books.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    menu_cat = Category.objects.all()
    return menu_cat

@register.simple_tag()
def get_articles():
    menu_art = Article.objects.all()
    return menu_art

@register.inclusion_tag('book/home_show')
def show_get_categories(filter):
    if filter == 0:
        list_cat = Book.objects.all()
    else:
        list_cat = Book.objects.filter(cat_id=filter)
    return  {'list_cat': list_cat, 'cid': filter}

@register.simple_tag()
def show_posts_cat():
    list_posts_cat = Article.objects.all()
    return list_posts_cat

@register.inclusion_tag('book/show_post')
def show_get_post(filter):
    if filter == 0:
        post = Articles.objects.all()
    else:
        post = Articles.objects.filter(slug=filter)
    return  {'post_sel': post, 'slug': filter}
