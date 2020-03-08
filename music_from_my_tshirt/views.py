"""
Views.
"""

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, TemplateView

from music_from_my_tshirt import forms, models


class HomePage(TemplateView):
    template_name = "music_from_my_tshirt/home_page.html"


class UserProfile(UserPassesTestMixin, ListView):
    """User profile view."""

    model = models.Song
    ordering = "-created"
    paginate_by = settings.USER_PROFILE_SONGS_PER_PAGE

    def test_func(self):
        return self.request.user.username == self.kwargs["username"]

    def get_queryset(self):
        self.queryset = models.Song.objects.filter(
            user__username=self.kwargs["username"]
        )
        return super().get_queryset()


class ShareSong(LoginRequiredMixin, CreateView):
    """Share song view."""

    model = models.Song
    form_class = forms.ShareSongForm
    success_url = "/"

    def form_valid(self, form):
        """
        Save the form, set the user for the song, add a message, and redirect to
        success page.
        """
        # pylint: disable=attribute-defined-outside-init
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.add_message(
            self.request,
            messages.INFO,
            "Shared {} by {}".format(self.object.title, self.object.artist),
        )
        return HttpResponseRedirect(self.get_success_url())
