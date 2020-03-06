"""Forms."""

from django import forms
from django.contrib.auth import forms as auth_forms

from allauth.account import forms as allauth_forms

from music_from_my_tshirt import models


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.User
        fields = ["username", "email"]


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = models.User
        fields = ["username", "email"]


class SignUpForm(allauth_forms.SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"


class LoginForm(allauth_forms.LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = "Email"


class ShareSongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = ["artist", "song", "url"]
        widgets = {"artist": forms.TextInput(), "song": forms.TextInput()}
