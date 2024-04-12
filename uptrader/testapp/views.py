from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Menu
from django.views.generic import ListView


# Create your views here.
def index(request): 
    return render(request, 'testapp/base.html')


def page(request, slug, id, path=None):
    menu_name = Menu.objects.filter(slug=slug)
    context={"slug":slug, "name":menu_name, "id": id}
    if path:
        context.update({"path":path})
    return render(request, 'testapp/page.html', context)

class MenuListView(ListView):
    model = Menu
    template_name = "testapp/page.html"
