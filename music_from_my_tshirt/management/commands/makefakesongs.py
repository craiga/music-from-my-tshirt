"""Command to create fake songs for a user."""

from django.core.management.base import BaseCommand

from faker import Faker

from music_from_my_tshirt import models


class Command(BaseCommand):
    """Create fake songs for a user."""

    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument("username", type=str)
        parser.add_argument("num_posts", type=int)

    def handle(self, *args, **options):
        """Handle a call to the command."""
        user = models.User.objects.get(username=options["username"])
        fake = Faker()
        for _ in range(0, options["num_posts"]):
            models.Song.objects.create(
                title=fake.name(), artist=fake.name(), url=fake.url(), user=user
            )
