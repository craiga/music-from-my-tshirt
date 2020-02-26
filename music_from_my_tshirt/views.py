"""
Views.
"""

from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "music_from_my_tshirt/home_page.html"
