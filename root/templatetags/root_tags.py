from django import template


register = template.Library()

@register.filter
def total_lessons(modules_manager):
    modules = modules_manager.all()
    return sum(module.lessons.count() for module in modules)