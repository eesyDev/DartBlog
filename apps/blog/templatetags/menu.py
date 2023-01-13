from django import template
from apps.blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {
        'categoies' : categories,
        'menu_class' : menu_class
    }
