from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from .models import Woomen, Category, TagPost, UploadFiles
from .forms import UploadFileForm
from .forms import AddPostForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .utils import DataMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class WoomenHome(DataMixin, ListView):
    # model = Woomen
    template_name = "woomen/index.html"
    context_object_name = 'posts' #атрибут для того чтобы его использовать в шаблоне иначе в шаблоне писать object_list
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Woomen.published.all().select_related('cat')
 

@login_required
def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'woomen/about.html',
                  {'title': 'О сайте', 'form': form})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


    
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'woomen/addpage.html'
    title_page = 'Добавление статьи'
    # success_url = reverse_lazy('home')# формирует url адрес в момент когда он нуже(в отличии от reverse)
    # инчае автоматически использует get_absolute_url класса AddPostForm

    # данная реализация привязвыет в пользователя к публикации в бд
    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)
    



class UpPage(DataMixin, UpdateView):
    model = Woomen
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'woomen/addpage.html'
    success_url = reverse_lazy('home')# формирует url адрес в момент когда он нуже(в отличии от reverse)
    # инчае автоматически использует get_absolute_url класса AddPostForm
    title_page = 'Редактирование статьи'



def login(request):
    return HttpResponse("Авторизация")



def contact(request):
    return HttpResponse("Обратная связь")



class ShowPost(DataMixin, DetailView):
    # model = Woomen
    template_name = 'woomen/post.html'
    context_object_name = 'post' #чтобы использовать в шаблоне
    slug_url_kwarg = 'post_slug' # чтобы использовать в маршруте

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'])


    def get_object(self, queryset=None):
        ''' Для того чтобы нельзя было просмотреть неопубликованну запись(все кроме неопубликованные)'''
        return get_object_or_404(
            Woomen.published, slug=self.kwargs[self.slug_url_kwarg]
            )
    


class WoomenCategory(DataMixin, ListView):
    template_name = "woomen/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Woomen.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(
            context,
            title='Категория - ' + cat.name,
            cat_selected=cat.pk
            )



class TagPostlist(DataMixin, ListView):
    template_name = "woomen/index.html"
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self):
        return Woomen.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(
            context,
            title=f'Тег {tag.tag}',
            cat_selected=None
            )
    
