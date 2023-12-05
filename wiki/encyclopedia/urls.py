from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index")
# ]

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newPage/", views.newPage, name="newPage"),
    path("edit/", views.edit, name="edit"),
    path("subEdit/", views.subEdit, name="subEdit"),
    path("rand/", views.rand, name="rand"),
]
