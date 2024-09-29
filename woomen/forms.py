from typing import Any
from django import forms
from .models import Husband, Category, Woomen
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

# валидация с помощью класса
# @deconstructible
# class RussianValidator():
#     ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
#     code = 'russian'

#     def __init__(self, messege=None) -> None:
#         self.messege = messege if messege else "Должны использоваться только русские символы, дефиз или пробел"
#     def __call__(self, value, *args: Any, **kwds: Any) -> Any:
#         if not set(value) <= set(self.ALLOWED_CHARS):
#             raise ValidationError(self.messege, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            empty_label="Категория не выбрана",
            label='Категория',
            )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(),
        empty_label="Не замужем",
        required=False,
        label='Муж',
        )
    class Meta:
        model = Woomen
        fields = [
            'title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags'
            ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {
            'slug': 'URL'
        }


    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "

    #     if not (set(title) <= set(ALLOWED_CHARS)):
    #         raise ValidationError("Должны присутствовать только русские символы, дефис и пробел.")


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')



#второй вариант исполнения формы(добавить статью)
# class AddPostForm(forms.Form):
#     title = forms.CharField(
#         max_length=255,
#         min_length=5,
#         label="Заголовок",
#         widget=forms.TextInput(attrs={'class': 'form-input'}),
#         validators=[
#             RussianValidator()
#         ],
#         error_messages={
#             'min_length': 'Слишком короткий заголовок',
#             'required': 'Без заголовка никак',
#         })
#     slug = forms.SlugField(
#         max_length=100,
#         label='URL',
#         validators=[
#             MinLengthValidator(5, message='Минимум 5 символов'),
#             MaxLengthValidator(100, message='Максимум 100 символов'),
#         ])
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),
#         required=False,
#         label='Контент',
#         )
#     is_published = forms.BooleanField(
#         required=False,
#         label='Статус',
#         initial=True,
#         )
#     cat = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         empty_label="Категория не выбрана",
#         label='Категория',
#         )
#     husband = forms.ModelChoiceField(
#         queryset=Husband.objects.all(),
#         empty_label="Не замужем",
#         required=False,
#         label='Муж',
#         )

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "

    #     if not (set(title) <= set(ALLOWED_CHARS)):
    #         raise ValidationError("Должны присутствовать только русские символы, дефис и пробел.")
