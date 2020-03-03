"""Context processors."""

from django.conf import settings


def sentry_dsn(request):
    return {"sentry_dsn": settings.SENTRY_DSN}


def canonical_host(request):
    return {"canonical_host": settings.ENFORCE_HOST}
