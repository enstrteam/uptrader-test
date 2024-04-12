from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Menu(MPTTModel):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, verbose_name="URL", db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, db_index=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.parent:
            return reverse("testapp:sub-page", kwargs={"path": "/".join([item.slug for item in self.get_ancestors()]), "slug": self.slug, "id":self.pk})
        else:
            return reverse("testapp:page", kwargs={"slug": self.slug, "id":self.pk})
