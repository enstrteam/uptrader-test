from django.urls import path, include

from . import views

app_name = "testapp"

extra_patterns = [
    path("<path:path>/<slug:slug>/<int:id>/", views.page, name="sub-page"),
    path("<slug:slug>/<int:id>/", views.page, name="page"),
]

urlpatterns = [
    path("", include(extra_patterns)),
    path("", views.index, name="index"),
]
