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


