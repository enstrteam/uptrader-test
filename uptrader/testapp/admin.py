from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Menu

# Register your models here.

class MenuAdmin(DjangoMpttAdmin):
    MPTT_ADMIN_LEVEL_INDENT = 30
    prepopulated_fields={"slug":("name",)}

admin.site.register(Menu, MenuAdmin)