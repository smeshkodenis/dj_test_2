"""
URL configuration for book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import *
from book import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_category, name='index'),
    path('cats/<int:cat_id>/', show_category, name='cat'),
    path('about/', about, name='about'),
    path('posts', PostsMain.as_view(), name = 'posts'),
    path('post_sel/<slug:post_slug>/', ShowPost.as_view(), name='post_sel'),
    path('add_page', addpage, name='addpage'),
    path('add_new_post_cat', add_new_post_cat, name='add_new_post_cat')
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)