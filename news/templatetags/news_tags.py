from django import template
from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_category.html')
def show_categories(arg1 = 'Здравствуйте,', arg2 = 'Медведев Денис Валерьевич'):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1':arg1, 'arg2':arg2 }

@register.inclusion_tag('news/list_category_burger.html')
def show_categories_burger(arg1 = 'Hello,', arg2 = 'Медведев Денис Валерьевич'):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1':arg1, 'arg2':arg2 }