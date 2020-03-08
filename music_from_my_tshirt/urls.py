"""URLs."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from music_from_my_tshirt import views

urlpatterns = [
    path("non-obvious-path/", admin.site.urls),
    path("account/", include("allauth.urls")),
    path("share-song", views.ShareSong.as_view(), name="share_song"),
    path("u/<str:username>", views.UserProfile.as_view(), name="user_profile"),
    path("", views.HomePage.as_view(), name="home_page"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
