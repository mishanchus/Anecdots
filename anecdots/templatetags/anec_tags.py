from django import template
from ..models import Category

register = template.Library()


# @register.simple_tag()
# def get_category():
#     return Category.objects.all()

@register.inclusion_tag('list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}