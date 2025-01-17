from django.urls import path, re_path, register_converter
from . import views
from . import convertes


register_converter(convertes.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.WoomenHome.as_view(), name="home"),
    path('about/', views.about, name="about"),
    path('addpage/', views.AddPage.as_view(), name="add_page"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>/', views.WoomenCategory.as_view(), name="category"),
    path('tag/<slug:tag_slug>/', views.TagPostlist.as_view(), name="tag"),
    path('edit/<slug:slug>/', views.UpPage.as_view(), name="edit"),
]

