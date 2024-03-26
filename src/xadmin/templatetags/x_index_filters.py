from django.template import Library

from .base import InclusionAdminNode

register = Library()

def x_index():
    is_app_list = True

    return {
        "is_app_list": is_app_list,
    }

@register.tag(name="x_index")
def ax_index_tag(parser, token):
    return InclusionAdminNode(
        parser, token, func=x_index, template_name="xindex.html"
    )