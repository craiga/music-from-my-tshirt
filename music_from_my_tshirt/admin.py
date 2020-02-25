"""Admin configuration."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from music_from_my_tshirt import forms, models


class User(UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.User
    list_display = ["email", "username"]


admin.site.register(models.User, User)
