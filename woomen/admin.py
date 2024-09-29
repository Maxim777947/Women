from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from .models import Woomen, Category
from django.utils.safestring import mark_safe

#пароль 1234, demen

class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'замужем'),
            ('single', 'Не замужем'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Woomen)
class WoomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'tags']
    # exclude = [] исключение отображаемых полей
    readonly_fields = ['post_photo'] #Не радактируемые поля
    # filter_horizontal = []  расширение отображаемого вида тега
    filter_vertical = ["tags"] # расширение отображаемого вида тега
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'post_photo', 'time_create', 'is_published', )
    list_display_links = ('title', )   #Кликабельные поля
    list_editable = ('is_published', )
    list_per_page = 5 #количестви показываемых записей
    ordering = ('time_create', 'title', )
    actions = ['set_published', 'set_draft'] # добавлене в действие
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description="Изображение", ordering="content")
    def post_photo(self, woomen: Woomen):
        if woomen.photo:
            return mark_safe(f"<img src='{woomen.photo.url}' width=50>")
        return 'Без фото'
    
    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Woomen.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")
 
    @admin.action(description="Снять c публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Woomen.Status.DRAFT)
        self.message_user(
            request, f"{count} записей снято с публикации.", messages.WARNING
            )# messages.WARNING добавление значка <!> перед собщеением о снятии


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')   #Кликабельные поля

# admin.site.register(Woomen, WoomenAdmin) способ без декоратора

