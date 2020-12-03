from django import template

register = template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None

# This is the model_name template filter. We can apply this in template as object|model_name to get the model name of an object