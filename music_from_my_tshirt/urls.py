"""URLs."""
from django.contrib import admin
from django.urls import path

urlpatterns = [path("non-obvious-path/", admin.site.urls)]
