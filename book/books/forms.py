from django import forms
from django.core.exceptions import ValidationError

from .models import *


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255, required=True, label='Заголовок')
    content = forms.CharField(max_length=1200, required=True, label='Содержание')
    cat = forms.ModelChoiceField(queryset=PostsCat.objects.all(), label='Категория')
    is_published = forms.BooleanField()
    # slug = AutoSlugField(unique=True, verbose_name="URL", populate_from='title') #добавил, когда боролся с отсутствием отображения слаг при добавлении статьи


class PostCatForm(forms.ModelForm):
    class Meta:
        model = PostsCat
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'text']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')

        if name and len(name) > 200:
            raise ValidationError('Длина имени превышает 200 символов')

        if email and len(email) > 200:
            raise ValidationError('Длина email превышает 200 символов')

        return name
