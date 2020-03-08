"""Models."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from model_utils.models import TimeStampedModel


class User(AbstractUser):
    def __str__(self):
        return self.email


class Song(TimeStampedModel):
    """A song. Probably from a user's t-shirt."""

    artist = models.TextField()
    title = models.TextField()
    url = models.URLField("URL")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} by {} shared by {} on {}".format(
            self.title, self.artist, self.user, self.created
        )
