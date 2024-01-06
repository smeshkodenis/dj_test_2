from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request, cat_id = 0):
    return render(request, 'book/index.html')

def categories(request, cat_id):
    return render(request, 'book/index.html', cat_id=cat_id)

def about(request):
    return render(request, 'book/about.html')

def posts(request):
    return render(request, 'book/posts.html')


def addpage(request):
    form = ArticleForm()
    return render(request, 'books.addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def show_category(request, cat_id=0):
    if cat_id == 0:
        list_cat = Book.objects.all()
    else:
        list_cat = Book.objects.filter(cat_id=cat_id)
    return render(request, 'book/home_show.html', {'list_cat': list_cat, 'cid': cat_id})

def show_post(request, post_slug):
    return render(request, 'book/show_post.html', post_slug)
