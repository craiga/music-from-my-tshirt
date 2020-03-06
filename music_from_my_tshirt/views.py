"""
Views.
"""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView

from music_from_my_tshirt import forms, models


class HomePage(TemplateView):
    template_name = "music_from_my_tshirt/home_page.html"


class ShareSong(LoginRequiredMixin, CreateView):
    """Share song view."""

    model = models.Song
    form_class = forms.ShareSongForm
    success_url = "/"

    def form_valid(self, form):
        """Once the valid form has been processed, set a message."""
        result = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.INFO,
            "Shared {} by {}".format(self.object.song, self.object.artist),
        )
        return result
