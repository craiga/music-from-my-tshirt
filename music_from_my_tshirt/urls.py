"""URLs."""

from django.contrib import admin
from django.urls import include, path

from music_from_my_tshirt import views

urlpatterns = [
    path("non-obvious-path/", admin.site.urls),
    path("account/", include("allauth.urls")),
    path("", views.HomePage.as_view(), name="home_page"),
]
