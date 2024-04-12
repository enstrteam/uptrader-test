from django import template
from testapp.models import Menu

register = template.Library()

@register.inclusion_tag("testapp/menu.html", takes_context=True)
def draw_menu(context, name):
    path = context.get("request").path
    menu = Menu.objects.all()
    tree_id = Menu.objects.get(name=name).tree_id
    menu_tree = menu.filter(tree_id = tree_id)
    
    if not path=="/":
        item = Menu.objects.get(pk=context["id"])
        return {'menu_list':menu_tree, "current_item": item}
    else: 
        return {'menu_list': menu_tree}

@register.inclusion_tag("testapp/title.html", takes_context=True)
def show_title(context, default_title=None):

    if not default_title:
        title = Menu.objects.get(pk=context["id"]).name
        return {
            "title": title,
        }
    else:
        return {
            "title": default_title
        }

@register.inclusion_tag("testapp/breadcrumbs.html", takes_context=True)
def breadcrumb(context):
    item = Menu.objects.get(pk=context["id"])
    return {
        "menu": item,      
    }

@register.filter
def active_class(item, current_item):
    if item == current_item:
        return "active"
    else:
        return "inactive"




