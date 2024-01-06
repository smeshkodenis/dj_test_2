from django import forms
from .models import *

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    content = forms.CharField(max_length=1200, required=True)
    cat = forms.ModelChoiceField(queryset=Article.objects.all())
    is_published = forms.BooleanField()
    #slug = AutoSlugField(unique=True, verbose_name="URL", populate_from='title') #добавил, когда боролся с отсутствием отображения слаг при добавлении статьи

    #class Meta:
     #   model = Article
      #  fields = '__all__'
