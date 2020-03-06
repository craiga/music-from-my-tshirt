"""Models."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from model_utils.models import TimeStampedModel


class User(AbstractUser):
    def __str__(self):
        return self.email


class Song(TimeStampedModel):
    artist = models.TextField()
    song = models.TextField()
    url = models.URLField("URL")
