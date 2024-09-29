# from typing import Any
# from django.db.models.base import Model as Model
# from django.db.models.query import QuerySet
# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
# from django.urls import reverse, reverse_lazy
# from django.template.loader import render_to_string
# from .models import Woomen, Category, TagPost, UploadFiles
# from .forms import UploadFileForm
# from .forms import AddPostForm
# from django.views import View
# from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
# from .utils import DataMixin


# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
# ]



# # Create your views here.
# # def index(request):
# #     slug = Woomen.published.all().select_related('cat')
# #     data = {
# #         'title': 'Главная страница',
# #         'menu': menu,
# #         'posts': slug,
# #         'cat_selected': 0,
# #     }
# #     return render(request, "woomen/index.html", context=data)


# class WoomenHome(DataMixin, ListView):
#     # model = Woomen
#     template_name = "woomen/index.html"
#     context_object_name = 'posts' #атрибут для того чтобы его использовать в шаблоне иначе в шаблоне писать object_list
#     title_page = 'Главная страница'
#     cat_selected = 0


#     # extra_context = {
#     #     'title': 'Главная страница',
#     #     'menu': menu,
#     #     'cat_selected': 0,
#     # }

#     def get_queryset(self):
#         return Woomen.published.all().select_related('cat')
 

#     # template_name = "woomen/index.html"
#     # extra_context = {
#     #     'title': 'Главная страница',
#     #     'menu': menu,
#     #     'posts': Woomen.published.all().select_related('cat'),
#     #     'cat_selected': 0,
#     # }


#     #не получилось (альтренатива выше) раздел 8.1
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
        
#     #     context['title'] = 'Главная страница'
#     #     context['menu'] = menu
#     #     context['posts'] = Woomen.published.all().select_related('cat')
#     #     context['cat_selected'] = int(self.request.GET.get('cat_id', 0))
#     #     return context


# # def handle_uploaded_file(f):
# #     with open(f"uploads/{f.name}", "wb+") as destination:
# #         for chunk in f.chunks():
# #             destination.write(chunk)


# def about(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # handle_uploaded_file(form.cleaned_data['file'])
#             fp = UploadFiles(file=form.cleaned_data['file'])
#             fp.save()
#     else:
#         form = UploadFileForm()
#     return render(request, 'woomen/about.html',
#                   {'title': 'О сайте', 'menu': menu, 'form': form})


# def page_not_found(request, exception):
#     return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# # def add_page(request):
# #     if request.method == 'POST':
# #         form = AddPostForm(request.POST, request.FILES)
# #         if form.is_valid():
# # # print(form.cleaned_data)коллекция введенных данных
# # # try:
# # #     Woomen.objects.create(**form.cleaned_data)
# # #     return redirect('home')
# # # except:
# # #     form.add_error(None, 'Ошибка добавления')
# #             form.save()
# #             return redirect('home')
# #     else:
# #         form = AddPostForm()
# #     data = {
# #         'menu': menu,
# #         'title': 'Добавление статьи',
# #         'form': form
# #         }
# #     return render(request, 'woomen/addpage.html', data)


# # class AddPage(View):
# #     def get(self, request):
# #         form = AddPostForm()
# #         data = {
# #             'menu': menu,
# #             'title': 'Добавление статьи',
# #             'form': form
# #         }
# #         return render(request, 'woomen/addpage.html', data)

# #     def post(self, request):
# #         form = AddPostForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('home')
# #         data = {
# #             'menu': menu,
# #             'title': 'Добавление статьи',
# #             'form': form
# #         }
# #         return render(request, 'woomen/addpage.html', data)


# # class AddPage(FormView):
# #     form_class = AddPostForm
# #     template_name = 'woomen/addpage.html'
# #     success_url = reverse_lazy('home')# формирует url адрес в момент когда он нуже(в отличии от reverse)
# #     extra_context = {
# #         'title': 'Добавление статьи',
# #         'menu': menu,
# #     }
# #     def form_valid(self, form):
# #         '''Соъраняет в БД введенную в форму инфу'''
# #         form.save()
# #         return super().form_valid(form)
    

# class AddPage(CreateView):
#     form_class = AddPostForm
#     # model = Woomen
#     # fields = '__all__'
#     template_name = 'woomen/addpage.html'
#     # success_url = reverse_lazy('home')# формирует url адрес в момент когда он нуже(в отличии от reverse)
#     # инчае автоматически использует get_absolute_url класса AddPostForm
#     extra_context = {
#         'title': 'Добавление статьи',
#         'menu': menu,
#     }


# class UpPage(UpdateView):
#     model = Woomen
#     fields = ['title', 'content', 'photo', 'is_published', 'cat']
#     template_name = 'woomen/addpage.html'
#     success_url = reverse_lazy('home')# формирует url адрес в момент когда он нуже(в отличии от reverse)
#     # инчае автоматически использует get_absolute_url класса AddPostForm
#     extra_context = {
#         'title': 'Редактирование статьи',
#         'menu': menu,
#     }




# def login(request):
#     return HttpResponse("Авторизация")


# def contact(request):
#     return HttpResponse("Обратная связь")


# # def show_post(request, post_slug):
# #     post = get_object_or_404(Woomen, slug=post_slug)
# #     data = {'title': post_slug.title,
# #             'menu': menu,
# #             'post': post,
# #             'cat_selected': 1}
# #     return render(request, 'woomen/post.html', data)


# class ShowPost(DataMixin, DetailView):
#     # model = Woomen
#     template_name = 'woomen/post.html'
#     context_object_name = 'post' #чтобы использовать в шаблоне
#     slug_url_kwarg = 'post_slug' # чтобы использовать в маршруте

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return self.get_mixin_context(context, title=context['post'])


#     def get_object(self, queryset=None):
#         ''' Для того чтобы нельзя было просмотреть неопубликованну запись(все кроме неопубликованные)'''
#         return get_object_or_404(
#             Woomen.published, slug=self.kwargs[self.slug_url_kwarg]
#             )
    


# # def show_category(request, cat_slug):
# #     category = get_object_or_404(Category, slug=cat_slug)
# #     posts = Woomen.published.filter(cat_id=category.pk).select_related('cat')
# #     data = {
# #         'title': f'Рубрика {category.name}',
# #         'menu': menu,
# #         'posts': posts,
# #         'cat_selected': category.pk,
# #     }
# #     return render(request, "woomen/index.html", context=data)


# class WoomenCategory(ListView):
#     template_name = "woomen/index.html"
#     context_object_name = 'posts'
#     allow_empty = False

#     def get_queryset(self) -> QuerySet[Any]:
#         return Woomen.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cat = context['posts'][0].cat
#         context['title'] = 'Категория - ' + cat.name
#         context['menu'] = menu
#         context['cat_selected'] = cat.pk
#         return context


# # def show_tag_postlist(request, tag_slug):
# #     tag = get_object_or_404(TagPost, slug=tag_slug)
# #     posts = tag.tags.filter(is_published=Woomen.Status.PUBLISHED).select_related('cat')
# #     print(posts)
# #     data = {
# #         'title': f'Тег {tag.tag}',
# #         'menu': menu,
# #         'posts': posts,
# #         'cat_selected': None,
# #     }
# #     return render(request, "woomen/index.html", context=data)


# class TagPostlist(ListView):
#     template_name = "woomen/index.html"
#     context_object_name = 'posts'
#     allow_empty = False
    
#     def get_queryset(self):
#         return Woomen.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
#         context['title'] = f'Тег {tag.tag}'
#         context['menu'] = menu
#         context['cat_selected'] = None
#         return context
    
