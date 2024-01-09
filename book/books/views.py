from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import *
from .forms import *
# Create your views here.
def index(request, cat_id = 0):
    return render(request, 'book/index.html')

def categories(request, cat_id):
    return render(request, 'book/index.html', cat_id=cat_id)

def about(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = MessageForm()
    return render(request, 'book/about.html', {'form': form})

'''def posts(request):
    return render(request, 'book/posts.html')'''

class PostsMain(ListView):
    model = Article
    template_name = 'book/posts.html'


def addpage(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            try:
                Article.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = ArticleForm()


    return render(request, 'book/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def add_new_post_cat(request):
    if request.method == 'POST':
        form = PostCatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostCatForm()


    return render(request, 'book/add_new_post_cat.html', {'form': form, 'title': 'Добавление новой категории статей'})

def show_category(request, cat_id=0):
    if cat_id == 0:
        list_cat = Book.objects.all()
    else:
        list_cat = Book.objects.filter(cat_id=cat_id)
    return render(request, 'book/home_show.html', {'list_cat': list_cat, 'cid': cat_id})

def show_post(request, post_slug):
    return render(request, 'book/show_post.html', {'post_slug':post_slug})

class ShowPost(DetailView):
    model = Article
    template_name = 'book/show_post.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
