from django import template
import woomen.views as views
from woomen.models import Category, TagPost
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('woomen/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gte=1)
    return {'cats': cats, 'cat_selected': cat_selected}
 

@register.inclusion_tag('woomen/list_tags.html')
def show_all_tags(cat_selected=0):
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gte=1)}
